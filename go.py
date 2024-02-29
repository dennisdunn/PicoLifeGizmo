from life.life import Machine
from life.display import LedMatrix
import life.patterns as patterns
import time

disp = LedMatrix()
ca = Machine()


ca.load(patterns.Blinker)

while True:
    ca.update()
    disp.setPixels(ca.cells)
    time.sleep(0.1)