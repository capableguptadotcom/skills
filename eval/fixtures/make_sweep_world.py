"""Generate eval/fixtures/session-sweep-large: a synthetic world too big to read by hand.

    python eval/fixtures/make_sweep_world.py

Deterministic. Planted findings:
- csv-export: loads on its own often; in 9 sessions the user pushes back with the same complaint
  (the header row is dropped). A recurring problem.
- db-migrations: an automatic skill that only ever runs when named. Its description does not trigger.
- invoice-themes: installed, never runs.
- Noise: follow-up requests that start with "Actually", pauses with "continue", ordinary uses.
Every session mentions the client (Orion) and a contact email, which must not leak.
"""

import json
import random
import shutil
from datetime import datetime, timedelta, timezone
from pathlib import Path

OUT = Path(__file__).resolve().parent / 'session-sweep-large'
SKILLS = {
    'diagnose': 'Use first for any bug.',
    'research': 'Answer a question from sources.',
    'review-change': 'Review a change before it merges.',
    'csv-export': 'Use when exporting report data to CSV.',
    'db-migrations': 'Database schema changes.',
    'invoice-themes': 'Pick a color theme for invoice PDFs.',
}
ASKS = {
    'diagnose': ['The Orion sync job fails with a timeout on large accounts.', 'Tests in billing/ fail since the upgrade.'],
    'research': ['Which queue library fits Orion billing?', 'Compare two PDF libraries for invoices.'],
    'review-change': ['Review my change before the PR.', 'Can you review the diff on this branch?'],
    'csv-export': ['Export the Orion monthly usage report to CSV.', 'Give me the invoices for March as a CSV file.'],
    'db-migrations': ['$db-migrations add a nullable region column to accounts', '$db-migrations rename plan_code'],
}
GOOD = ['thanks', 'great, ship it', 'looks right', 'perfect']
FOLLOW = ['Actually, can you also add a summary table?', 'Actually, also send me the totals.', 'Wait, also cover refunds.']
HEADER = ['No, the header row is missing again. The CSV must start with the column names.',
          "That's wrong, you dropped the header row. Keep it.",
          'No, the file has no header line. Our importer needs the header.']


def codex_session(sid, when, skill, ask, reply, agent):
    path = OUT / f'homes/codex/sessions/{when:%Y/%m/%d}/rollout-{when:%Y-%m-%dT%H-%M-%S}-{sid}.jsonl'
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = when.isoformat().replace('+00:00', 'Z')
    lines = [{'timestamp': stamp, 'type': 'session_meta', 'payload': {'id': sid, 'timestamp': stamp,
              'cwd': '/work/orion-billing', 'source': 'vscode', 'cli_version': '0.170.0'}},
             {'type': 'event_msg', 'payload': {'type': 'user_message',
              'message': f'{ask} Contact: ops@orion-client.example'}},
             {'type': 'event_msg', 'payload': {'type': 'exec_command_begin',
              'command': ['bash', '-lc', f'cat /home/dev/.agents/skills/{skill}/SKILL.md'],
              'parsed_cmd': [{'type': 'read', 'path': f'/home/dev/.agents/skills/{skill}/SKILL.md'}]}},
             {'type': 'event_msg', 'payload': {'type': 'agent_message', 'message': agent}}]
    if reply == 'PAUSE':
        lines += [{'type': 'event_msg', 'payload': {'type': 'turn_aborted'}},
                  {'type': 'event_msg', 'payload': {'type': 'user_message', 'message': 'can you continue'}}]
    else:
        lines.append({'type': 'event_msg', 'payload': {'type': 'user_message', 'message': reply}})
    path.write_text('\n'.join(json.dumps(l) for l in lines) + '\n', encoding='utf-8')


def main():
    rng = random.Random(7)
    if OUT.exists():
        shutil.rmtree(OUT)
    start = datetime(2026, 9, 1, 9, tzinfo=timezone.utc)
    plan = (['diagnose'] * 60 + ['research'] * 70 + ['review-change'] * 40 + ['csv-export'] * 30
            + ['db-migrations'] * 8)
    rng.shuffle(plan)
    header_left = 9
    for n, skill in enumerate(plan):
        when = start + timedelta(hours=7 * n + rng.randint(0, 5), minutes=rng.randint(0, 59))
        sid = f'cccccccc-{n:04d}-4000-8000-{n:012d}'
        ask = rng.choice(ASKS[skill])
        agent = f'Done with the {skill.replace("-", " ")} task.'
        roll = rng.random()
        if skill == 'csv-export' and header_left and roll < 0.6:
            reply, header_left = rng.choice(HEADER), header_left - 1
            agent = 'Wrote usage.csv with one row per account.'
        elif roll < 0.12:
            reply = rng.choice(FOLLOW)
        elif roll < 0.18:
            reply = 'PAUSE'
        else:
            reply = rng.choice(GOOD)
        codex_session(sid, when, skill, ask, reply, agent)
    assert header_left == 0, 'not every header complaint was planted'
    for name, description in SKILLS.items():
        folder = OUT / 'homes/skills' / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: {description}\n---\n\nStub.\n',
                                         encoding='utf-8')
    (OUT / 'homes/claude/projects').mkdir(parents=True, exist_ok=True)
    (OUT / 'homes/claude/projects/.keep').write_text('', encoding='utf-8')
    print(f'{len(plan)} sessions in {OUT}')


if __name__ == '__main__':
    main()
