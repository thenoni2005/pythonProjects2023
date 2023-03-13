#ANTHONY TRUJILLO and BRODY CARTER#
#10/12/2022#
#OREGON TRAIL#
import winsound
import random

from settings import *
from asciiArt import *



nameList = ['Joe','Joahn','Jane','John','Joester','Joestar','Jonathan']
nameSet = set(nameList)
charMoney = ""
partyMembers = []
charDifferences = ("""Traveling to Oregon isnt easy!\nBut if youre a banker/nyoull have more money for supplies and servies\nthan a carpenter or a farmer.\n\nHowever, the harder you have to try, the more points you deserve!\nTherefor, the farmer earns the greatest number of points\nand banker the least""")

def playSound():
    clearScreen()
    winsound.beep(440,300)

def managementOptions():
    clearScreen()
    print("Yes management")

def highScores():
    clearScreen()
    print("But can he beat goku\ndidnt think so..")

def loreScreen():
    clearScreen()
    print("A very deep, rugged, and rocky trail, its almost like nature doesnt care about you")

def gameQuit():
    clearScreen()
    choice = displayMenu(["Yes","No"],"are you sure you want to quit? ")
    if choice ==1:
        print("Old spice Whistle.... pa pa pa powa ")
        input("press enter to continue")
        quit()
    else:
        return

def clearScreen():
    print(" "*10000)

def displayMenu(options,question):
    print(ribbon)
    print(question)
    for i in range(len(options)):
        print(str.format("\t({0}.) ------------ {1:<30}",i+1,options[i]))
    print(ribbon)
    while True:
        choice = input("What would you like to do?: ")
        if choice.isnumeric():
            choice = int(choice)
            if choice <= len(options) and choice > 0:
                return choice
            else:
                print("not in the correct Range")
        else:
            print("you need to enter a number between 1"+str(len(options)))




def titleScreen():
    while True:
        print(gameTitle)

        choice = displayMenu(["Travel the Oregon trail","Learn about the trail","Top ten",
            "Sound options","Choose management options","Quit"],"You may:")
        if choice == 1:
            return
        elif choice == 2:
            loreScreen()
        elif choice == 3:
            highScores()
        elif choice == 4:
            playSound()
        elif choice == 5:
            managementOptions()
        elif choice == 6:
            gameQuit()

def jobSelection():
    while True:

        choice = displayMenu(["Be a banker from Boston","Be a carpenter","Be a farmer from Illinois",
            "Find out the differences"],"You may:")
        if choice == 1:
            charMoney = (1600)

        elif choice == 2:
            charMoney = (800)

        elif choice == 3:
            charMoney = (400)

        elif choice == 4:
            print (charDifferences)
        break

        return charMoney,choice

def partyNames():
    nameList = ("Joe","Joahn","Jane","John","Joester","Joestar","Jonathan","Joey","Janite","Jacky")
    while True:
        clearScreen()
        playerName = input("What is the first name of the wagon leader?  :")
        if playerName == "":
            playerName = (random.choice(nameList))
        memberOne = input("What is the name of your First party member?  :")
        if memberOne == "":
            memberOne = (random.choice(nameList))
        memberTwo = input("What is the name of your Second party member?  :")
        if memberTwo == "":
            memberTwo = (random.choice(nameList))
        memberThree = input("What is the name of your Third party member?  :")
        if memberThree == "":
            memberThree = (random.choice(nameList))
        memberFour = input("What is the name of your Fourth party member?  :")
        if memberFour == "":
            memberFour = (random.choice(nameList))
        print(playerName)
        print(memberOne)
        print(memberTwo)
        print(memberThree)
        print(memberFour)
        nameCheck = input("Are the names correct? Y/N:")
        if nameCheck == "Y":
            break
        elif nameCheck == "N":
            return
        return playerName,memberOne,memberTwo,memberThree,memberFour

def startMonthSelection():
    choice = displayMenu(["March","April","May","June","July","ask for advice"],"Kumalala")
    startMonth = []
    if choice == 1:
        month = 3
        day = 1
        year = 1867
    elif choice == 2:
        month = 4
        day = 1
        year = 1867
    elif choice == 3:
        month = 5
        day = 1
        year = 1867
    elif choice == 4:
        month = 6
        day = 1
        year = 1867
    elif choice == 5:
        month = 7
        day = 1
        year = 1867
    elif choice == 6:
        print("attend a public meeting held\br for folks with the California -\br Oregon fever. You're told:\br if you leave too early, there\br won't bne any grass for your\br oxen to eat. If you leave too\br late, you may not get to Oregon\br before winter comes. If you\br leave at just the right time,\br there will be green grass and\br the weather will still be cool." )

    return startMonth
def shop(money):
    inventory =[]
    bill = 0.00
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]
    choices = ["Oxen","Food","Cloths","Ammo","Waggon Parts","Check Out"]
    messages = ["""There are 2 oxen in a yoke;
                I recomend at least 3 yokes.
                I charge $40 a yoke""",
               """I recomend you take 200 pounds
                       of food for for each member in
                       your Party I charge $0.20 per pound
                       """,
               """
                       You will need warm clothing for
                       the trip I recommend taking 3 sets
                       of clothes per person in your party
                       Each set is $10.00
                       """,
               """
                       I sell boxes of ammo for $2.00
                       per box each box has 20 bullets
                       """
               ]
    questions = ["how many yokes would you like to buy","How many pounds of food do you Want",
                 "How many sets of clothes do you Want","How many boxes of ammo do you Want"]


    print("Before leaving Independence you should buy Equipment and Supplies.")
    print(str.format("you have ${:.2f} in cash to make this trip", money))
    input("Press Enter to Continue")
    print("remember you can buy supplys along the way so you dont have to spend it all now")
    input("Press Enter to Continue")
    while True:
        print("Welcome to the General Store")
        print("Here is a list of things you can buy")
        print(RIBBON)
        for i in range(len(choices)):
            print(str.format("\t{}:{:<20} ${:<10.2f}",i+1,choices[i],spent_on_items[i]))
        print(str.format("Total Bill so far   ${:.2f}", spent_on_items[len(spent_on_items)-1]))
        print(str.format("Total funds avalable:     ${:.2f}", money - bill))
        print(RIBBON)

        choice = getNumberInRange("What would you like to buy?",1,len(choices))
        if choice == 1:# buy oxen
            oxen,spent_on_items = buyGoods(spent_on_items,money,"ox",messages,questions)
            inventory.insert(0,oxen)


        elif choice == 2:# buy food
            food,spent_on_items= buyGoods(spent_on_items,money,"food",messages,questions)
            inventory.insert(1,food)

        elif choice == 3:# buy clothing
            cloths,spent_on_items = buyGoods(spent_on_items,money,"cloths",messages,questions)
            inventory.insert(2,cloths)

        elif choice == 4:# buy ammo
            ammo,spent_on_items = buyGoods(spent_on_items,money,"ammo",messages,questions)
            inventory.insert(3, ammo)

        elif choice == 5:# buy parts
            parts,spent_on_items = buyParts(spent_on_items,money)
            inventory.insert(4,parts)

        elif choice == 6:# check out
            if spent_on_items[len(spent_on_items)-1] <= money:
                if inventory[0] >= 1:
                    total_Wheels = 0
                    total_axles = 0
                    total_tongues = 0
                    total_tarps = 0
                    for part in inventory[4]:
                        if part == "Wagon Wheel":
                            total_Wheels +=1
                        elif part == "Wagon axle":
                            total_axles+=1
                        elif part == "Wagon Tongue":
                            total_tongues+=1
                        elif part == "Wagon Tarp":
                            total_tarps+=1

                    print(str.format("""
                    you have purchased 
                    {} yokes of oxen
                    {} pounds of food
                    {} sets of clothing
                    {} boxes of ammo
                    and the following wagon parts
                    {} Wheels
                    {} Axles
                    {} Tongues
                    {} Tarps                 
                    """,inventory[0]/2,inventory[1],inventory[2],inventory[3]/20,total_Wheels,total_axles,total_tongues,total_tarps))
                    choice = display_menu(["yes","no"], "is this correct")
                    if choice == 1:
                        money -= spent_on_items[len(spent_on_items) - 1]
                        return inventory
                    else:
                        print("Start over then")
                        inventory = []
                        bill = 0.00
                        spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
                        continue
                else:
                    print("you must have at least 1 oxen to travel Start shoping over")
                    inventory = []
                    bill = 0.00
                    spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
                    continue
            else:
                print("you dont have enough money Start over")
                inventory = []
                bill = 0.00
                spent_on_items = [0.00, 0.00, 0.00, 0.00, 0.00, bill]
                continue

def buyGoods(spent_on_items,money,good,messages,questions):
    if good == "ox":
        index = 0
        price = 40
        multiplyer = 2
    elif good == "food":
        index = 1
        price = 0.20
        multiplyer = 1
    elif good == "cloths":
        index = 2
        price = 10
        multiplyer = 1
    elif good == "ammo":
        index = 3
        price = 2
        multiplyer = 20
    # clear the amount spent on goods from the current bill
    currentbill = spent_on_items[len(spent_on_items) - 1]
    currentbill = currentbill - spent_on_items[index]

    # update the spent on items list with updated values
    spent_on_items[len(spent_on_items) - 1] = currentbill
    spent_on_items[index] = 0.00

    goods = 0
    print(messages[index])
    print(str.format("Total Bill so far:        ${:.2f}", spent_on_items[len(spent_on_items) - 1]))
    answer = getNumberInRange(questions[index], 1, money / price)

    cost = answer * price
    goods = answer * multiplyer

    currentbill += cost

    spent_on_items[index] = cost
    spent_on_items[len(spent_on_items) - 1] = currentbill
    return goods, spent_on_items


#
def buyParts(spent_on_items,money):
    print("""
    It is a good idea to have a few
    Spare parts for your wagon on hand 
    you never know what can happen on 
    the trail and a broken down 
    wagon can be a death sentence""")

    partsInventory = []
    currentBill = spent_on_items[len(spent_on_items)-1]
    currentBill = currentBill - spent_on_items[4]

    spent_on_items[4] = 0.00
    partsBill = 0.00
    options = ["Wagon wheel","Wagon Axle","Wagon tongue","Tarp","back to main shop"]
    partsCost = [10.00,20.00,50.00,12.00,partsBill]
    while True:
        partsCost[len(partsCost)-1] = partsBill
        print("here is a list of things you can buy")
        for i in range(len(options)):
            print(str.format("{}.    {:20}    {:.2f}",i+1,options[i],partsCost[i]))
        print(str.format("Total bill so far:           ${:.2f}",partsBill))
        print(str.format("Total funds available:           ${:.2f}",money))

        choice = getNumberInRange("what is your choice",1,len(options))
        if choice == 1:
            parts = getNumberInRange("how many wagon wheels do you want?",0,)
            for i in range(parts)
                partsInventory.append("Wagon Wheel")
            partsBill += partsCost[0]*parts
        elif choice == 2:
            parts = getNumberInRange("how many wagon wheels do you want?", 0, )
            for i in range(parts)
                partsInventory.append("Wagon Wheel")
            partsBill += partsCost[1] * parts
        elif choice == 3:
            parts = getNumberInRange("how many wagon wheels do you want?", 0, )
            for i in range(parts)
                partsInventory.append("Wagon Wheel")
            partsBill += partsCost[2] * parts
        elif choice == 4:
            parts = getNumberInRange("how many wagon wheels do you want?", 0, )
            for i in range(parts)
                partsInventory.append("Wagon Wheel")
            partsBill += partsCost[3] * parts
        elif choice == 5:
                currentBill
                partsInventory.append("Wagon Wheel")
            partsBill += partsCost[4] * parts

def game():





    #Game code goes here
    titleScreen()
    jobSelection()
    partyNames()
    startMonthSelection()