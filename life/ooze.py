import asyncio

class PrimodialOoze:
    def __init__(self, machine, display, seed):
        self._engine = machine
        self._engine.load(seed)
        self._display = display

    def syncTick(self):
        self._engine.update()
        self._display.setPixels(self._engine._cells)

    async def tick(self,sec):
        self.syncTick()
        await asyncio.sleep(sec)


if __name__ == '__main__':
    import time
    from life.machine import Machine
    from life.display import LedMatrix
    from life.patterns import R_Pentonimo as seed

    life = Machine()
    world = LedMatrix()

    ooze = PrimodialOoze(life, world, seed)

    async def timeline():
        while True:
            await ooze.tick(0.1)

    t1 = asyncio.run(timeline())

    