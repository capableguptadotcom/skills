"""Bounded event-order model, with deterministic replay against Lease.claim."""
import asyncio
from itertools import permutations
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from lease import Lease


def schedules():
    events = ("a:read", "a:resume", "b:read", "b:resume")
    return [order for order in permutations(events)
            if all(order.index(f"{w}:read") < order.index(f"{w}:resume")
                   for w in ("a", "b"))]


def model(order, initial_owner=None):
    owner = initial_owner
    free = {}
    results = {}
    for event in order:
        worker, phase = event.split(":")
        if phase == "read":
            free[worker] = owner is None
        else:
            results[worker] = free[worker]
            if free[worker]:
                owner = worker
    return results, owner


async def replay(order, lease_type=Lease, initial_owner=None):
    lease = lease_type()
    lease.owner = initial_owner
    entered = {w: asyncio.Event() for w in ("a", "b")}
    released = {w: asyncio.Event() for w in ("a", "b")}
    tasks = {}
    results = {}

    async def checkpoint(worker):
        entered[worker].set()
        await released[worker].wait()

    for event in order:
        worker, phase = event.split(":")
        if phase == "read":
            tasks[worker] = asyncio.create_task(
                lease.claim(worker, lambda w=worker: checkpoint(w)))
            await entered[worker].wait()
        else:
            released[worker].set()
            results[worker] = await tasks[worker]
    return results, lease.owner


async def check():
    failures = []
    for order in schedules():
        for initial_owner in (None, "existing"):
            predicted = model(order, initial_owner)
            actual = await asyncio.wait_for(replay(order, initial_owner=initial_owner), 2)
            assert actual == predicted, (order, initial_owner, predicted, actual)
            if sum(actual[0].values()) > (1 if initial_owner is None else 0):
                failures.append((order, actual))
    print("model/code correspondence: pass (6 schedules x 2 initial states)")
    print(f"lease uniqueness: {'FAIL' if failures else 'pass'} ({len(failures)} violating schedules)")
    if failures:
        print(f"counterexample: {failures[0]}")
    return not failures


if __name__ == "__main__":
    raise SystemExit(0 if asyncio.run(check()) else 1)
