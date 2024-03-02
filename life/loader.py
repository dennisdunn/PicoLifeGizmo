class Load:
    def __init__(self):
        pass

    @staticmethod
    def file(machine, path):
        f = open(path)
        str = f.read()
        f.close()
        Load.source(machine, str)
    
    @staticmethod
    def source(machine, str):
        cells = eval(str)
        Load.list(machine, cells)

    @staticmethod
    def list(machine, tuples):
        newCells = {}
        for cell in tuples:
            newCells[cell] = 0
        machine._cells = newCells