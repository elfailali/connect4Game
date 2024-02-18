from Classes.grid import Grid
from Classes.jeton import Jeton


if __name__ == '__main__':
        game = Grid()
        jeton = Jeton()
        grid = game.createGrid()
        game.displayGrid(grid)

        game.insertJetonToCase(grid, jeton.color[0], 3, 3)
        game.displayGrid(grid)
