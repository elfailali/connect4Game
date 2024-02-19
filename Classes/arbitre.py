from Classes.player import Player
from Classes.grid import Grid

class Arbitre:
    winnerPlayer = ""

    def setWinnerPlayer(self, player):
        self.winnerPlayer = player

    def setJetonInColumn(self, grid, playerJetonColor, column):
        if Grid().isValidLocation(grid, column):
            line = Grid().getNextOpenLine(grid, column)
            Grid().insertJetonToCase(grid, playerJetonColor, line, column)


