import asyncio

class PrimodialOoze:
    def __init__(self, machine, display, period):
        self._engine = machine
        self._display = display
        self._period = period

    async def evolve(self, seed):
        self._engine.load(seed)
        while True:
            self._engine.update()
            self._display.setPixels(self._engine._cells)
            await asyncio.sleep(self._period)    


if __name__ == '__main__':
    try:
        from life.machine import Machine
        from life.display import LedMatrix
        from life.pattern import Glider as seed

        engine = Machine()
        world = LedMatrix()
        ooze = PrimodialOoze(engine, world, 0.1)
        
        asyncio.run(ooze.evolve(seed))
        
    except KeyboardInterrupt:
        pass