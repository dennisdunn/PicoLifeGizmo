
class Machine:
    def __init__(self):
        self._cells = {}

    def load(self, tuples):
        self._cells = {}
        for xy in tuples:
            self._cells[xy] = 0

    def update(self):
        next = {}
        counts = self._countNeighbors()

        for xy, count in counts.items():
            if xy in self._cells:  # is alive
                if count == 2 or count == 3:  # stayin' alive
                    next[xy] = self._cells[xy] + 1
                else:
                    continue  # unalived
            else:  # unalive
                if count == 3:
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
    from life.patterns import Blinker as pattern

    life = Machine()

    life.load(pattern)

    for _ in range(5):
        life.update()
        print(life._cells)
