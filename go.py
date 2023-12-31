import asyncio
from life.machine import Machine
from life.display import LedMatrix
from web.server import Server
import lib.mm_wlan as mm_wlan
from config import Configuration as Cfg

disp = LedMatrix()
ca = Machine()
server = Server(disp, ca)

ca.cells = {
    (1, 0): "blue",
    (2, 1): "blue",
    (0, 2): "blue",
    (1, 2): "blue",
    (2, 2): "blue"
}


async def ca_update():
    while True:
        ca.update()
        disp.setPixels(ca.cells)
        await asyncio.sleep(0.1)

if __name__ == '__main__':
    mm_wlan.connect_to_network(Cfg['ssid'], Cfg['password'])
    asyncio.create_task(ca_update())
    server.serve(Cfg['port'])
