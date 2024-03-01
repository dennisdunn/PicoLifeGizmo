import asyncio
import bluetooth

from lib.ble_advertising import advertising_payload
from lib.ble_uart_peripheral import BLEUART

from life.ooze import PrimodialOoze
from life.machine import Machine
from life.display import LedMatrix
from life.patterns import Glider as seed

try:
    engine = Machine()
    world = LedMatrix()
    ooze = PrimodialOoze(engine, world, 0.1)
    
    ble = bluetooth.BLE()
    uart = BLEUART(ble, "PicoLife")

    def on_rx():
        source = uart.read().decode().strip()
        engine.load(eval(source))
        
    uart.irq(handler=on_rx)

    asyncio.run(ooze.evolve(seed))
except KeyboardInterrupt:
    uart.close()
    pass