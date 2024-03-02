import asyncio
import bluetooth

from lib.ble_uart_peripheral import BLEUART

from life.ooze import PrimodialOoze
from life.machine import Machine
from life.display import LedMatrix
from life.loader import Load

DATA_FILE = 'pattern.txt'

def save(data):
    f = open(DATA_FILE,'w')
    f.write(data)
    f.close()

try:
    engine = Machine()
    world = LedMatrix()
    ooze = PrimodialOoze(engine, world, 0.1)
    
    ble = bluetooth.BLE()
    uart = BLEUART(ble, "PicoLife")

    buffer = ""
    def on_rx():
        global buffer
        str = uart.read().decode().strip()
        print(str)
        if str.startswith("["):
            buffer = str
        else:
            buffer += str
        if buffer.endswith("]"):
            save(buffer)
            Load.source(engine, buffer)
        
    uart.irq(handler=on_rx)

    Load.file(engine, DATA_FILE)
    asyncio.run(ooze.evolve())
except KeyboardInterrupt:
    pass

uart.close()