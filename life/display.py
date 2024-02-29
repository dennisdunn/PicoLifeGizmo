from picounicorn import PicoUnicorn
from life.color import Colors
<<<<<<< HEAD

=======
>>>>>>> 075be2268161a69fb692fb334828f0dc3b79b9b7

class LedMatrix:
    def __init__(self) -> None:
        self._board = PicoUnicorn()
        self._height = self._board.get_height()
        self._width = self._board.get_width()

    def size(self):
        return (self._width, self._height)

    def clear(self):
        for x in range(self._width):
            for y in range(self._height):
                self.setPixel((x, y), "black")

    def setPixel(self, xy, color):
        (x, y) = xy
        (r, g, b) = Colors[color]
        self._board.set_pixel(x % self._width, y %
                              self._height, r, g, b)  # toroidal display

    def setPixels(self, cells):
        for xy, color in cells.items():
            self.setPixel(xy, color)


if __name__ == "__main__":
    cells = {
        (7, 3): "blue",
        (7, 4): "blue",
        (7, 5): "blue"
    }

    disp = LedMatrix()
    disp.setPixels(cells)
