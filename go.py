from life.life import Machine
from life.display import LedMatrix
import time

disp = LedMatrix()
ca = Machine()

ca.cells = {
        (7, 3): "blue",
        (7, 4): "blue",
        (7, 5): "blue"
    }

while True:
    ca.update()
    disp.setPixels(ca.cells)
    time.sleep(0.5)