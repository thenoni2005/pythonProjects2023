# ANTHONY TRUJILLO
# 9/26/2022
# GUESS MY NUMBER

import random


# GLOBALS VARIABLES



# 1 pick a random number in given range
# get guess from user
# check if guess == number
# if guess < number
# tell user to guess higher
# if guess > number
# tell user to guess lower

def checkForIntInput(question,min,max):
    number =""
    #get a good number within a given range and validate the data before it returns it#
    while(True):
        number = input(question)
        if(number.isdigit()) and ((int(number) >= min) and (int(number) <= max)):
            number = int(number)
            return number

        else:
            print("not a good input")





def main():
    min = 1
    max = 10
    number = 0
    guess = 0
    trys = 3
    number = random.randint(min,max)
    playing = True
    while True:
        diff = input("Continue??? in easy?, Medium?, or Hard,")
        if("e" in diff.lower().strip()):
            min = 1
            max = 10
            trys = 3
            break
        elif("m" in diff.lower().strip()):
            min = 10
            max = 50
            trys = 5
            break
        elif ("h" in diff.lower().strip()):
            min = 50
            max = 150
            trys = 15
            break
        else:
            print("not a good input")



    guess = checkForIntInput("Pick a number between " + str(min) + " and " + str(max) + " :  ", min, max)
    while(guess != number and trys>1):
        if(guess < number):
            print("Haha wrong guess higher")
            trys -= 1
        elif(guess > number):
            print("Wrong! guess lower")
            trys -= 1
        guess = checkForIntInput("Pick a number between " + str(min) + " and " + str(max) + " :  ", min, max)

    if (trys > 1):
        print("you got it great job")
    else:
        print("you suck at this")
    answer = input("You could get jiggy with it and play again answer yes or no")
    if("n" in answer.lower()):
        playing = False
main()






















