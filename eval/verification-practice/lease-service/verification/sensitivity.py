"""Clean scratch control and deliberately broken scratch variant; no product writes."""
import asyncio
from pathlib import Path
from model import replay, schedules


async def check():
    shipped = (Path(__file__).resolve().parents[1] / "lease.py").read_text()
    unsafe = "        free = self.owner is None\n        await checkpoint()"
    safe = "        await checkpoint()\n        free = self.owner is None"
    assert shipped.count(unsafe) == 1
    clean_source = shipped.replace(unsafe, safe)
    broken_source = clean_source.replace(safe, unsafe)
    assert broken_source == shipped
    for label, source, expected in (("clean scratch control", clean_source, 0),
                                    ("deliberate stale-read mutation", broken_source, 4)):
        namespace = {}
        exec(compile(source, f"<{label}>", "exec"), namespace)
        violations = 0
        for order in schedules():
            results, _ = await asyncio.wait_for(replay(order, namespace["Lease"]), 2)
            violations += sum(results.values()) > 1
        assert violations == expected, (label, violations, expected)
        print(f"{label}: {violations}/6 violating schedules (expected {expected})")


if __name__ == "__main__":
    asyncio.run(check())
