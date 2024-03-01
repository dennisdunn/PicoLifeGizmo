import asyncio
import bluetooth

from lib.ble_uart_peripheral import BLEUART

from life.ooze import PrimodialOoze
from life.machine import Machine
from life.display import LedMatrix

DATA_FILE = 'life/pattern.txt'

try:
    engine = Machine()
    world = LedMatrix()
    ooze = PrimodialOoze(engine, world, 0.1)
    
    ble = bluetooth.BLE()
    uart = BLEUART(ble, "PicoLife")

    def on_rx():
        source = uart.read().decode().strip()
        f = open(DATA_FILE,'w')
        f.write(source)
        engine.load(eval(source))
        
    uart.irq(handler=on_rx)

    f = open(DATA_FILE)
    seed = eval(f.read())
    asyncio.run(ooze.evolve(seed))
except KeyboardInterrupt:
    uart.close()
    pass