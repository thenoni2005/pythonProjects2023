import pygame as pg
from Settings import *
from gameClass import *

def main():

    pg.init()
    while True:
        game = Game()

        game.showStart()

        game.startGameLoop()

        game.showOver()

        x = game.showOver()
        if x == "end":
            break

    pg.quit()

    quit()



main()