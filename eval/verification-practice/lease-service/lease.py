class Lease:
    def __init__(self):
        self.owner = None

    async def claim(self, worker, checkpoint):
        free = self.owner is None
        await checkpoint()
        if not free:
            return False
        self.owner = worker
        return True
