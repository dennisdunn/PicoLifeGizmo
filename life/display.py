from picounicorn import PicoUnicorn
from picographics import PicoGraphics, DISPLAY_UNICORN_PACK
from life.colormap import WheelMap as ColorMap


class LedMatrix:
    def __init__(self) -> None:
        self._picounicorn = PicoUnicorn()
        self._graphics = PicoGraphics(display=DISPLAY_UNICORN_PACK)
        self._width, self._height = self._graphics.get_bounds()

    def clear(self):
        pen = self._graphics.create_pen(0,0,0)
        self._graphics.set_pen(pen)
        self._graphics.clear()

    def setPixel(self, xy, age):
        (x, y) = xy
        (r, g, b) = ColorMap[age % len(ColorMap)]
        pen = self._graphics.create_pen(r,g,b)
        self._graphics.set_pen(pen)
        self._graphics.pixel(x % self._width, y % self._height)  # toroidal display

    def setPixels(self, cells):
        self.clear()
        for xy, age in cells.items():
            self.setPixel(xy, age)
        self._picounicorn.update(self._graphics)


if __name__ == "__main__":
    import time
    display = LedMatrix()

    for (r, g, b) in ColorMap:
        pen = display._graphics.create_pen(r,g,b)
        display._graphics.set_pen(pen)
        display._graphics.clear()
        display._picounicorn.update(display._graphics)
        time.sleep_ms(25)

