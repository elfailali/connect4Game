from Classes.player import Player
from Classes.app import App
from Classes.arbitre import Arbitre
from Classes.grid import Grid
import sys


def newPlayer(num):
    name = input(f"Enter tha Name of a player number {num}: ")
    color = input(f"Choose a color for {name} (red): ")
    player = Player(name, color)
    return player


while True:
    player1 = newPlayer(1)
    player2 = newPlayer(2)

    # ⚠️: Verify that the two players are different

    arbitre = Arbitre()
    grid = Grid().createGrid()

    game = App(arbitre, player1, player2, grid)
    game.startGame()

    rejouer = input("Play again ? (y/n) : ")
    if rejouer.lower() != "y":
        print("Au revoir !")
        break
        # sys.exit(0)
