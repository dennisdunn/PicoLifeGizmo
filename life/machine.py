class Machine:
    def __init__(self):
        self._cells = {}

    def load(self, xys):
        self._cells = {}
        for xy in xys:
            self._cells[xy] = 0

    def update(self):
        next = {}
        counts = self._countNeighbors()

        for xy in counts:
            if xy in self._cells:  # is alive
                if counts[xy] == 2 or counts[xy] == 3:  # stayin' alive
                    next[xy] = self._cells[xy]
                    next[xy] += 1
                else:
                    continue  # unalived
            else:  # unalive
                if counts[xy] == 3:
                    next[xy] = 0  # newly alived

        self._cells = next

    def _countNeighbors(self):
        """For each cell, update the count of
        cells who have this one as a neighbor.

        Returns:
            dict: A map of (x,y) -> count
        """
        deltas = [-1, 0, 1]
        counts = {}

        for xy in self._cells:
            (x, y) = xy
            for dx in deltas:
                for dy in deltas:
                    ckey = (x+dx, y+dy)
                    if xy == ckey:
                        continue
                    if ckey in counts:  # defaultdict(int)
                        counts[ckey] += 1
                    else:
                        counts[ckey] = 1

        return counts


if __name__ == '__main__':
    import time
    from life.display import LedMatrix
    from life.patterns import Beacon as pattern

    life = Machine()
    display = LedMatrix()

    life.load(pattern)

    while True:
        life.update()
        display.setPixels(life._cells)
        time.sleep(0.1)
