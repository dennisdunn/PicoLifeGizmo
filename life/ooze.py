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
        
    async def evolve(self, sec):
        while True:
            await ooze.tick(sec)


if __name__ == '__main__':
    from life.machine import Machine
    from life.display import LedMatrix
    from life.patterns import Glider as seed

    engine = Machine()
    world = LedMatrix()

    ooze = PrimodialOoze(engine, world, seed)
    
    asyncio.run(ooze.evolve(0.1))

    