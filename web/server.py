from lib.microdot import Microdot
import lib.mm_wlan as mm_wlan
from web.mime import MimeTypes


class Server:
    def __init__(self, display, ca):
        self._display = display
        self._ca = ca

    def _read(self, path):
        try:
            with open(path) as fd:
                return fd.read()
        except Exception as e:
            print(e, path)

    def serve(self, port):
        app = Microdot()

        @app.get('/')
        async def index(request):
            return static_file(request, 'index.html')

        @app.get('<path:path>')
        async def static_file(request, path):
            content = self._read('./public/'+path)
            type = path.split('.')[1]
            return content, {'Content-Type': MimeTypes[type]}

        @app.put('/cells')
        async def set_cells(request):
            cells = {}
            for cell in request.json:
                cells[(cell['x'], cell['y'])] = "green"
            self._display.clear()
            self._ca.cells = cells

        app.run(port=port)


if __name__ == '__main__':
    mm_wlan.connect_to_network('TMOBILE-43DD', 'peekaboo99')
    server = Server(None, None)
    server.serve(5000)
