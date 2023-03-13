#ANTHONY TRUJILLO
#10/6/2022
#STORY BOARD

import random

def gameLoop(story, question, room1, room2, room3, room4, room5, room6, room7, room8, room9, room10,  insults):
    while True:
        print(story)
        while True:
            choice = input(question)
            if (choice in room1):
                story = " room 1"
                break
            elif choice in room2:
                story = " room 2"
                break
            if (choice in room3):
                story = " room 3"
                break
            if (choice in room4):
                story = " room 4"
                break
            if (choice in room5):
                story = " room 5"
                break
            if (choice in room6):
                story = " room 6"
                break
            if (choice in room7):
                story = " room 7"
                break
            if (choice in room8):
                story = " room 8"
                break
            if (choice in room9):
                story = " room 9"
                break
            if (choice in room10):
                story = " room 10"
                break

            else:
                print(random.choice(insults))




gameLoop("starting","give me an input", [1,"one","yes"],[2,"two","no"], ["you stink"])
