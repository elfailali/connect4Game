import unittest
from Classes.analyser import Analyser
from Classes.grid import Grid


class AnalyserTestCase(unittest.TestCase):

    def givenNewGridWhenDrawMatchThenReturnFalse(self):
        gridClass = Grid()
        grid = gridClass.createGrid()
        Analyser().drawMatch(grid)
        self.assertEqual(Analyser().drawMatch(grid), False)


if __name__ == '__main__':
    unittest.main()
