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

    def isValidLocation(self, grid, column):
        return grid[6-1][column] == Grid().defaultValueOfJeton

    def getNextOpenLine(self, grid, col):
        for line in range(Grid.getLines(self)):
            if grid[line][col] == Grid().defaultValueOfJeton:
                return line
    def insertJetonToCase(self, grid, jeton, line, column):
        if column < 7 and line < 6:
            if self.isValidLocation(grid, column):
                grid[line][column] = jeton
                print("jeton est : "+str(jeton))
            else:
                raise ValueError("Impossible, You chose a full Column!")

        else:
            raise ValueError("Error: Column index must be less than 7 and line index must be less than 6")



