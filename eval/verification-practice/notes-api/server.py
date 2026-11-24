import argparse
import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("--port", type=int, default=0)
p.add_argument("--data-dir", required=True)
a = p.parse_args()
data = Path(a.data_dir)
data.mkdir(parents=True, exist_ok=True)
notes = data / "notes.json"
ready = threading.Event()

def initialize():
    time.sleep(2)
    if not notes.exists():
        notes.write_text("[]", encoding="utf-8")
    ready.set()

class Handler(BaseHTTPRequestHandler):
    def reply(self, status, body):
        raw = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if self.path == "/health":
            self.reply(200, {"process": "up"})
        elif self.path == "/notes":
            if not ready.is_set():
                self.reply(503, {"error": "initializing"})
            else:
                self.reply(200, json.loads(notes.read_text(encoding="utf-8")))
        else:
            self.reply(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/notes":
            self.reply(404, {"error": "not found"})
        elif not ready.is_set():
            self.reply(503, {"error": "initializing"})
        else:
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            rows = json.loads(notes.read_text(encoding="utf-8"))
            note = {"id": len(rows) + 1, "title": body["title"]}
            rows.append(note)
            notes.write_text(json.dumps(rows), encoding="utf-8")
            self.reply(201, note)

threading.Thread(target=initialize, daemon=True).start()
server = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
print(f"port={server.server_port}", flush=True)
server.serve_forever()
