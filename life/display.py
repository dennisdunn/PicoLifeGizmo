from picounicorn import PicoUnicorn
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK


class LedMatrix:
    def __init__(self):
        self._picounicorn = PicoUnicorn()
        self._graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK)

        self._width, self._height = self._graphics.get_bounds()

    def clear(self):
        pen = self._graphics.create_pen(0, 0, 0)
        self._graphics.set_pen(pen)
        self._graphics.clear()

    def setPixel(self, xy, age):
        (x, y) = xy
        pen = self._graphics.create_pen_hsv(self._age2hue(age), 1.0, 1.0)
        self._graphics.set_pen(pen)
        self._graphics.pixel(x % self._width, y % self._height)  # toroidal display

    def setPixels(self, cells):
        self.clear()
        for xy, age in cells.items():
            self.setPixel(xy, age)
        self._picounicorn.update(self._graphics)

    def _age2hue(self, age):
        return 0.6666 - 0.0026 * (age % 256)


if __name__ == "__main__":
    try:
        import time
        display = LedMatrix()

        for h in range(256):
            pen = display._graphics.create_pen_hsv(0.66-0.0026*h, 1.0, 1.0) # Math is Magic
            display._graphics.set_pen(pen)
            display._graphics.clear()
            display._picounicorn.update(display._graphics)
            time.sleep_ms(25)

        display.clear()
    except KeyboardInterrupt:
        pass