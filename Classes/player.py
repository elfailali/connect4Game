from Classes.grid import Grid
from Classes.jeton import Jeton
from Classes.analyser import Analyser


class Player:

    def __init__(self, name, color):
        jeton = Jeton(color)
        self.playerJetonColor = jeton.getColor()
        self.playerName = name

    def getPlayerJetonColor(self):
        return str(self.playerJetonColor)

    def setPlayerName(self, name):
        self.playerName = name

    def getPlayerName(self):
        return self.playerName

    def askForPlayerInputColumn(self):
        while True:
            try:
                column = int(input(f"{self.getPlayerName()}, choose a column[0,6]: "))
                if 7 > column >= 0:
                    return column
            except ValueError:
                print("Invalid input. Please enter a valid column number.")

