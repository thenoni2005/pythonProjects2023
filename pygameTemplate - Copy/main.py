

from scripts.game import *
# Run everything (calling your code)
def main():
    while True:

        game = Game()
        game.startScreen()
        game.gameLoop()
        game.endScreen()

        break

    pg.quit()
    quit()




if __name__ == '__main__':
    main()