from JackBlackClasses import *
from cards import *
from player_file import *
import random

def main():
    print("\t\tWelcome to the fun zone; fun only fun!\n")
    names = []
    num = askNumber("how many players are playing (1 - 7)",low = 1, high = 8)
    for i in range(num):
        name = input("Player "+str(i+1)+"Enter your name")
        names.append(name)

    game = JackBlackGames(names)
    play = None
    while play != "n":
        game.play()
        play = ask_yes_no("\nDo you wanna play a game?: ")






main()