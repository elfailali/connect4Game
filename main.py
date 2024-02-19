from Classes.player import Player
from Classes.app import App
from Classes.arbitre import Arbitre
from Classes.grid import Grid
import sys

name = input("Enter tha Name of the first player: ")
color = input(f"Choose a color for {name} (red): ")
player1 = Player(name, color)

name = input("Enter tha Name of the second player: ")
color = input(f"Choose a color for {name} (blue): ")
player2 = Player(name, color)


arbitre = Arbitre()
grid = Grid().createGrid()

"""game = Game(arbitre, player1, J2, grid)
game.start_game()

rejouer = input("rejouer ? (o/n)")

if rejouer == "o":
    game.start_game()
elif rejouer == "n":
    print("à la prochaine")"""

while True:
    game = App(arbitre, player1, player2, grid)
    game.start_game()

    rejouer = input("Voulez-vous rejouer ? (o/n) : ")
    if rejouer.lower() != "o":
        print("Au revoir !")
        sys.exit()