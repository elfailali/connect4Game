import unittest
from Classes.grid import Grid
from Classes.jeton import Jeton


class GridTestCase(unittest.TestCase):
    def testShouldCreateGrid(self):
        grid = Grid()
        self.assertEqual(grid.getLines(), 6)
        self.assertEqual(grid.getColumns(), 7)

    def testShouldVerifyThatJetonInTheRightPosition(self):
        gridClass = Grid()
        grid = gridClass.createGrid()
        jeton = Jeton()
        line = 2
        column = 5
        gridClass.insertJetonToCase(grid, jeton, line, column)

        self.assertEqual(grid[line][column], jeton)


if __name__ == '__main__':
    unittest.main()
