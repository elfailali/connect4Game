from Classes.grid import Grid


class Analyser:

    def winningMove(self, grid, player):
        jeton = player.getPlayerJetonColor()
        for column in range(Grid().getColumns() - 3):
            for line in range(Grid().getLines()):
                if grid[line][column] == jeton and \
                        grid[line][column + 1] == jeton and \
                        grid[line][column + 2] == jeton and \
                        grid[line][column + 3] == jeton:
                    return True

        for line in range(Grid().getLines() - 3):
            for column in range(Grid().getColumns()):
                if grid[line][column] == jeton and \
                        grid[line + 1][column] == jeton and \
                        grid[line + 2][column] == jeton and \
                        grid[line + 3][column] == jeton:
                    return True

        for column in range(Grid().getColumns() - 3):
            for line in range(Grid().getLines() - 3):
                if grid[line][column] == jeton and \
                        grid[line + 1][column + 1] == jeton and \
                        grid[line + 2][column + 2] == jeton and \
                        grid[line + 3][column + 3] == jeton:
                    return True

        for column in range(Grid().getColumns() - 3):
            for line in range(3, Grid().getLines()):
                if grid[line][column] == jeton and \
                        grid[line - 1][column + 1] == jeton and \
                        grid[line - 2][column + 2] == jeton and \
                        grid[line - 3][column + 3] == jeton:
                    return True

    def drawMatch(self, grid):
        for line in range(Grid().getLines()):
            for column in range(Grid().getColumns()):
                if grid[line][column] == Grid().defaultValueOfJeton:
                    return False
        return True

