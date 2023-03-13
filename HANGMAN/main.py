#ANTHONY. TRUJILLO
#11/14/2022
#HANGMAN

from game import *
import settings as settings

def main():
    while True:
        choice = settings.display_menu(["play Tic Tax Evade","Play Hang Man","RPS","Quit"],"What would you like to do?")
        if choice == 1:
            gameTikTacToe()
        elif choice == 2:
            game()
            if settings.guesses < len(settings.HANGMAN):
                print("you win Good Job")
            else:
                print("you Lose")
        elif choice == 3:
            rockPaperScissors()
        else:
            settings.game_quit()



main()