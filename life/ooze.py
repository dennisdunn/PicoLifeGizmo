import asyncio

class PrimodialOoze:
    def __init__(self, machine, display, period=0.1):
        self._engine = machine
        self._display = display
        self._period = period

    async def evolve(self):
        while True:
            self._engine.update()
            self._display.setPixels(self._engine._cells)
            await asyncio.sleep(self._period)    


if __name__ == '__main__':
    try:
        from life.machine import Machine
        from life.display import LedMatrix
        from life.loader import Load

        str = '[(1,0),(2,1),(0,2),(1,2),(2,2)]'
        
        engine = Machine()
        world = LedMatrix()
        ooze = PrimodialOoze(engine, world)

        Load.source(engine, str)
        
        asyncio.run(ooze.evolve())
        
    except KeyboardInterrupt:
        pass