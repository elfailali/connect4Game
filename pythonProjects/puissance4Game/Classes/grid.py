class Grid:
    defaultValueOfJeton = "o"

    def __init__(self):
        self.lines = 6
        self.columns = 7

    def getLines(self):
        return self.lines

    def getColumns(self):
        return self.columns

    def createGrid(self):
        return [[self.defaultValueOfJeton for _ in range(self.getColumns())] for _ in range(self.getLines())]

    def displayGrid(self, grid):
        print('   '.join(str(x) for x in range(self.columns)))
        for line in grid:
            print("_" * self.lines * 4)
            print(*line, sep=' | ')
        print('_' * self.lines * 5)

    def insertJetonToCase(self, grid, jeton, line, column):
        grid[line][column] = jeton
