#ANTHONY TRUJILLO
#10/10/2022
#TEXT ADVENTURE

#Creating variables like health and such
import random
lives = 3
health = 100
stamina = 100
insults = "You stink","You are the reason shampoo has instructions","Would you do it again for klondite bar","XBOX LIVE!!!","You think pepper is spicy don't you"
room1 = ("you are in a bedroom with a twin sized bed , a desk, a window, and a door that leads out")
room2 = ("an empty hallway the room behind you dissapears all you see is white walls,doors, and an infinitely peircing blindness of white")
room3 = ("")
room4 = ("")
room5 = ("")
room6 = ("")
room7 = ("")
room8 = ("")
room9 = ("")
room10 = ("")

def room1():
    while True:
        print(art1)
        print(1story1)
        choice = input(question1)
        if choice == "1":
            room2()

#Basic print lines to introduce players
def main():
    room1()
    playing = True
userName = input("what is your name? :")

print("goodluck " + str(userName) +" you are currently stuck inside a dream find your way out")
print("lives "+str(lives))
print("health "+str(health))
print("stamina "+str(stamina))
print("this is your current life force use it wisely, every movement you make will cost you stamina dont waste it")
print("If your stamina reaches ZERO you die.")
print("-----DreamScape-----")
print("-by: Anthony.T------")
print(room1)
r1 = input("what is your move: ")
if r1 == ("open door")
    print("you open the door and enter" +str(room2)+)




main()
