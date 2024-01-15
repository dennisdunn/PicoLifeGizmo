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

    def on_receive(msg):
        try:
            seed = eval(msg)
            if isinstance(seed,list) and isinstance(seed[0],tuple):
                engine.load(seed)
        except Exception as _e:
            print(_e)

    p.on_write(on_receive)

    asyncio.run(ooze.evolve(seed))
except KeyboardInterrupt:
    pass