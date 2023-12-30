from life import life
from life import display
import time

disp = display.LedMatrix()
ca = life.Machine()

ca.cells = {
        (7, 3): "blue",
        (7, 4): "blue",
        (7, 5): "blue"
    }

while True:
    ca.update()
    disp.setPixels(ca.cells)
    time.sleep(0.5)