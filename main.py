import asyncio
from life.ooze import PrimodialOoze
from life.machine import Machine
from life.display import LedMatrix
from life.patterns import Glider as seed

engine = Machine()
world = LedMatrix()
ooze = PrimodialOoze(engine, world, 0.1)

asyncio.run(ooze.evolve(seed))

