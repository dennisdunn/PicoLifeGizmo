class Machine:
    def __init__(self):
        self.cells = {}

    def update(self):
        next = {}
        alive = self._filter(self.cells)
        counts = self._countNeighbors(alive)
        for key in counts.keys():
            if key in alive:  # is alive
                if counts[key] == 2 or counts[key] == 3:  # stayed alive
                    next[key] = self.cells[key]
                else:
                    next[key] = "black"  # unalived
            else:  # unalive
                if counts[key] == 3:
                    next[key] = "blue"  # newly alived

        self.cells = next

    def _countNeighbors(self, cells):
        """For each cell, update the count of
        cells who have this one as a neighbor.

        Returns:
            dict: A map of (x,y) -> count
        """
        deltas = [-1, 0, 1]
        counts = {}

        for key in cells.keys():
            (x, y) = key
            for dx in deltas:
                for dy in deltas:
                    ckey = (x+dx, y+dy)
                    if key == ckey:
                        continue
                    if ckey in counts:
                        counts[ckey] += 1
                    else:
                        counts[ckey] = 1
        return counts

    def _filter(self, cells):
        """Remove all of the dead cells.

        Args:
            cells (_type_): _description_
        """
        alive = dict(cells)
        for key in cells:
            if (cells[key] == "black"):
                del alive[key]
        return alive
