from Classes.analyser import Analyser
from Classes.grid import Grid
import sys


class App:
    def __init__(self, arbitre, player1, player2, grid):
        self.arbitre = arbitre
        self.player1 = player1
        self.player2 = player2
        self.grid = grid
        self.gameOver = False

    def turnPlay(self, player):
        column = player.askForPlayerInputColumn()
        self.arbitre.setJetonInColumn(self.grid, player.getPlayerJetonColor(), column)
        Grid().displayGrid(self.grid)
        if Analyser().winningMove(self.grid, player):
            self.arbitre.setWinnerPlayer(player.getPlayerName())
            print(f"The winner is {player.getPlayerName()}")
            self.gameOver = True

    def startGame(self):
        Grid().displayGrid(self.grid)
        turn = 0
        while not self.gameOver:
            if turn == 0:
                self.turnPlay(self.player1)
            else:
                self.turnPlay(self.player2)

            turn += 1
            turn = turn % 2

        if Analyser().drawMatch(self.grid):
            print(f"DRAW: The match is end with no winner")
            sys.exit(0)
