import asyncio
import bluetooth

from lib.ble_advertising import advertising_payload
from lib.ble_simple_peripheral import BLESimplePeripheral

from life.ooze import PrimodialOoze
from life.machine import Machine
from life.display import LedMatrix
from life.patterns import Glider as seed

try:
    engine = Machine()
    world = LedMatrix()
    ooze = PrimodialOoze(engine, world, 0.1)
    
    ble = bluetooth.BLE()
    p = BLESimplePeripheral(ble, "PicoLife")

    buffer = ""
    def on_receive(msg):
        global buffer
        text = msg.decode('UTF-8')
        if text[0] == '[' :
            buffer = text
        else:
            buffer+=text
        if buffer[len(buffer)-1]==']':
            seed = eval(buffer)
            engine.load(seed)

    p.on_write(on_receive)

    asyncio.run(ooze.evolve(seed))
except KeyboardInterrupt:
    pass