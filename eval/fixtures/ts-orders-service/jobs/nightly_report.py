"""Finance's nightly report: revenue per day and canceled orders, from exports/orders.jsonl."""
import json
import sys
from collections import defaultdict
from datetime import datetime


def load(path):
    with open(path, encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def report(rows):
    revenue, canceled = defaultdict(int), 0
    for row in rows:
        day = datetime.fromisoformat(row["placedAt"].replace("Z", "+00:00")).date()
        if row["status"] == "canceled":
            canceled += 1
        elif row["status"] == "paid":
            revenue[day] += row["total_cents"]
    lines = [f"{day}  ${cents / 100:.2f}" for day, cents in sorted(revenue.items())]
    return lines + [f"canceled orders: {canceled}"]


if __name__ == "__main__":
    print("\n".join(report(load(sys.argv[1] if len(sys.argv) > 1 else "exports/orders.jsonl"))))
