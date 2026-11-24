from itertools import permutations

def check():
    for workers in permutations(("a", "b")):
        owner = None
        successes = []
        for worker in workers:
            if owner is None:
                owner = worker
                successes.append(worker)
        assert len(successes) <= 1, (workers, successes)
    print("lease uniqueness: pass (two workers, atomic claims)")

if __name__ == "__main__":
    check()
