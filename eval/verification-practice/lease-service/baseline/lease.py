class Lease:
    def __init__(self):
        self.owner = None

    async def claim(self, worker, checkpoint):
        if self.owner is not None:
            return False
        self.owner = worker
        return True
