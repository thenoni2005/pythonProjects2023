import random

from asciiArt import *
from settings import *
import winsound





def clear_screen():
    print("\n"*10000)





def display_menu(options,question):
    print(ribbon)
    print(question)
    for i in range(len(options)):
        print(str.format("\t({0}.) ___________ {1:<30}",i+1,options[i]))
    print(ribbon)
    while True:
        choice = input("What would you like to do? ")
        if choice.isnumeric():
            choice = int(choice)
            if choice <= len(options) and choice > 0:
                return choice
            else:
                print("not in the correct Range")
        else:
            print("you need to enter a number between 1 and "+str(len(options)))





def getNumberInRange(question,min,max):
    while True:
        x = input(question)
        try:
            x = int(x)
        except:
            print("not a number")
            continue
        if x >= min and x <= max:
            return x
        else:
            print("not in Range")





def game_quit():
    clear_screen()
    choice = display_menu(["Yes","No"],"Are you sure you want to quit?")
    if choice == 1:
        print("Good by")
        input("Press Enter to Continue")
        quit()
    else:
        return





def lore_screen():
    clear_screen()
    print("""
    Try taking aa journey by covered wagon
    across 2000 + miles of Plains, Rivers,
    and Mountains. TRY!!!!!
    \n
    On the Plains will you slosh your oxen
    through mud and water-filled ruts? Or 
    will you traverse through dust six inches
    deep?
    \n
    How will you cross the River? if you 
    have the money, you might take a ferry
    (if there is a ferry). Or you can take
    a chance and ford the river and hope 
    you and your wagon aren't swallowed
    alive!
    """)
    input("Press Enter to Continue")

    print("""
    What about supplies? Well, if you're
    low on food you can hunt. You might get
    a Buffalo... you might. And there are 
    bear in the Mountains.
    \n
    you can try navigating 
    the Columbia River, but if running the 
    rapids with a makeshift raft makes you
    queasy better take the Barlow Road.
    \n
    If for some reason you dont survive --
    your wagon burns, or thieves steal your 
    oxen, or you run out of provisions, or you
    die of disease dont give up! try again
    and again until your name is on the Oregon
    Top Ten 
    """)
    input("Press Enter to Continue")
    clear_screen()





def high_scores():
    clear_screen()
    for i in range(10):
        print(str.format("\t({0:<2}) Score: {1:<10} Name: {2:<10}", i + 1, "000000", "Null"))
    input("Press Enter to Continue")




def play_sound():
    for i in range(5):
        winsound.Beep(900, 250)
        winsound.Beep(500, 250)
        winsound.Beep(960, 250)
        winsound.Beep(870, 250)
        winsound.Beep(900, 250)
    input("Press Enter to Continue")
    clear_screen()



def managment_Opt():
    clear_screen()
    choice = display_menu(["clear top ten", "Developer info"], "you may:")
    if choice == 1:
        print("Cleared")
        input("Press Enter to Continue")
    elif choice == 2:
        print("Anthony. Trujillo and Heavy inspiration from Mr.Broadbent")
        print("Average Oregon Trail enjoyer")
        input("Press Enter to Continue")



def prof_info():
    clear_screen()
    print("""
    Traveling the Oregon trail isn't easy!
    but if you're a banker, you'll have more
    money for supplies and services than a 
    carpenter or a farmer.

    However, the harder you have to work,
    the more points you deserve! therefore
    the farmer earns the greatest amount of 
    points and the banker earns the least.
    """)
    input("Press Enter to Continue")
    clear_screen()



def title_screen():
    clear_screen()
    while True:
        print(gameTitle)
        choice = display_menu(["Travel the Oregon Trail", "Learn about the Trail ", "Top Ten",
                               "Sound options", "Choose Management Options", "Quit"], "You may:")
        if choice == 1:
            return
        elif choice == 2:
            lore_screen()
        elif choice == 3:
            high_scores()
        elif choice == 4:
            play_sound()
        elif choice == 5:
            managment_Opt()
        elif choice == 6:
            game_quit()



def prof_selection():
    while True:
        clear_screen()
        choice = display_menu(["Be a Banker from Boston","Be a Carpenter from Ohio","Be a Farmer from Illinois"
                          ,"Be a citizen from Ohio","Find out the Differences between these choices"],
                      "Many Kinds of People made the trip To Oregon\nWho would you like to be?")
        if choice == 1:
            prof = "Banker"
            money = 1500
            diff = "Easy"
            break
        elif choice == 2:
            prof = "Carpenter"
            money = 1000
            diff = "Medium"
            break
        elif choice == 3:
            prof = "Farmer"
            money = 500
            diff = "Hard"
            break
        elif choice == 4:
            prof = "Kumalala"
            money = 690000000
            diff = "Cheating"
            break
        elif choice == 5:
            prof_info()
    return prof,money,diff



def party_namming():
    party_members = []
    random_names = ["Joe","Jack","Jill","Jim","Joahn","John","Jane","Savesta"]
    while True:
        clear_screen()
        player_name = input("What is your party leaders Name?")
        if len(player_name)>=3:
            break
        else:
            print("you must enter a valid name")

    while True:
        numInParty = input("How many people are in your party? must be a number between 1 and 5")
        if numInParty.isnumeric():
            numInParty = int(numInParty)
            if numInParty > 1 and numInParty <= 5:
                break
            else:
                print("must be a number between 1 and 5")
        else:
            print("must be a number")

    for i in range(numInParty):
        name = input("Enter party members name")
        if len(name) < 3:
            name = random.choice(random_names)
            random_names.remove(name)
        party_members.append(name)
    party_members.insert(0,player_name)
    return player_name,party_members




def start_month_selection():


    return month, day, year




def shop(money):
    inventory =[]
    bill = 0.00
    spent_on_items = [0.00,0.00,0.00,0.00,0.00,bill]
    choices = ["Oxen","Food","Cloths","Ammo","Waggon Parts","Check Out"]
    messages = ["""There are 2 oxen in a yoke;
                I reccomend at least 3 yokes.
                I charge $40 a yoke""",
               """I reccomend you take 200 pounds
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
        print(str.format("Total funds available:     ${:.2f}", money - bill))
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
            try:
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
                            return inventory, money
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
            except:
                print("YOU NEED TO BUY AN ITEM! NO ONE SURVIVES THE TRAIL WITHOUT FOOD AND LIVES TO TELL THE TALE")
                continue





def buyGoods(spent_on_items,money,good,messages,questions):
    if good == "ox":
        index = 0
        price = 40
        multiplier = 2
    elif good == "food":
        index = 1
        price = 0.20
        multiplier = 1
    elif good == "cloths":
        index = 2
        price = 10
        multiplier = 1
    elif good == "ammo":
        index = 3
        price = 2
        multiplier = 20
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
    goods = answer * multiplier

    currentbill += cost

    spent_on_items[index] = cost
    spent_on_items[len(spent_on_items) - 1] = currentbill
    return goods, spent_on_items




def buyParts(spent_on_items,money):

    print("""
    It is a good idea to have a few
    Spare parts for your wagon on hand
    you never know what can happen on
    the trail and a broken down
    wagon can be a death sentence
    """)
    parts_inventory = []
    spent_on_items[len(spent_on_items)-1] = spent_on_items[len(spent_on_items)-1] - spent_on_items[4]

    spent_on_items[4] = 0.00
    parts_bill = 0.00
    options = ["Wagon Wheel","Wagon axle","Wagon Tongue","Wagon Tarp","back to main shop"]
    parts_cost = [10.00,20.00,50.00,12.7251,parts_bill]
    while True:
        parts_cost[len(parts_cost)-1] = parts_bill
        print("Here is a list of things you can buy")
        for i in range(len(options)):
            print(str.format("{}.    {:20}     ${:.2f}",i+1,options[i],parts_cost[i]))
        print(str.format("Total Bill so far:        ${:.2f}", parts_bill))
        print(str.format("Total funds available:     ${:.2f}", money))

        choice = getNumberInRange("what is you choice",1,len(options))
        if choice == 1:
            parts = getNumberInRange("how many wagon Wheels do you want?",0,3)
            for i in range(parts):
                parts_inventory.append(options[0])
            parts_bill += parts_cost[0]*parts
        elif choice == 2:
            parts = getNumberInRange("how many Wagon axles do you want?", 0, 3)
            for i in range(parts):
                parts_inventory.append(options[1])
            parts_bill += parts_cost[1] * parts
        elif choice == 3:
            parts = getNumberInRange("how many Wagon Tongues do you want?", 0, 3)
            for i in range(parts):
                parts_inventory.append(options[2])
            parts_bill += parts_cost[2] * parts
        elif choice == 4:
            parts = getNumberInRange("how many wagon tarps do you want?", 0, 3)
            for i in range(parts):
                parts_inventory.append(options[3])
            parts_bill += parts_cost[3] * parts
        elif choice == 5:
            print(spent_on_items)
            spent_on_items[len(spent_on_items)-1] += parts_bill
            spent_on_items[4] = parts_bill
            print(spent_on_items)
            break
    return parts_inventory,spent_on_items

def cur_day(day,month):
    month = month
    MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    month_index = 0
    for m in range(len(MONTHS)):
        if MONTHS[m] == month:
            month_index = m
    if month_index >= len(MONTHS):
        month_index = -1

    day += 1
    if month in ["March","May","July","August","October","December"]:
        if day > 31:
            month = MONTHS[month_index+1]
            day = 1
    elif month == "February":
        if day > 28:
            month = MONTHS[month_index + 1]
            day = 1
    else:
        if day > 30:
            month = MONTHS[month_index + 1]
            day = 1
    date = str(month) + "/" + str(day) + "/" + str(2022)

    return day,month,date

def get_weather():
    WEATHER = ["Good","Good","Fair","Fair","Fair","Fair","Fair","Poor","Poor","Poor",]
    weather = random.choice(WEATHER)
    if weather == "Good":
        mod = 1
    elif weather == "Poor":
        mod = .25
    else:
        mod = .5
    return weather, mod

def eat(rations,food,members):
    food -= (3 * len(members))*rations
    if food <= 0:
        food = 0
    return food

def get_health(health_value,members):
    number = random.randint(1, 100)
    health_value -= 10
    sick = ""
    if number >= 90:
        health = "sick"
        conditions = ["the *#*^'s","Drowding","Cold","covid","flu","Exaustion"]
        sick = random.choice(conditions)
        if sick == conditions[0]:
            health_value -=15
        elif sick == conditions[1]:
            health_value -= 100
        elif sick == conditions[2]:
            health_value -= 10
        elif sick == conditions[3]:
            health_value -= 50
        elif sick == conditions[4]:
            health_value -= 20
        elif sick == conditions[5]:
            health_value -= 5

    if health_value <= 0:
        if sick =="":
            "Starvation"
        if len(members)>1:
            number = random.randint(1,len(members)-1)
            print(members[number]+" Has died from "+sick)
            members.remove(members[number])
            health_value = 100
        else:
            #game over
            print("you have Died")
            input()
            game_quit()

    if health_value > 80:
        health = "Good"
    elif health_value < 45:
        health = "Poor"
    else:
        health = "Fair"
    if health == "Good":
        health_mod = 1
    elif health == "Poor":
        health_mod = .25
    else:
        health_mod = .5
    return health, health_value, members,health_mod

def todays_travel(weather_mod,health_mod,pace):
    miles = 0
    high = int((25)*weather_mod+health_mod)
    low = int((5)*weather_mod+health_mod)
    miles = random.randint(low,high)*pace

    return miles

def change_pace():
    pace = 1
    choice = display_menu(["Fast pace","Normal pace","Slow pace"],"what Pace wuould you like to set?")
    if choice == 1:
        pace = 1
    elif choice  == 2:
        pace = .5
    else:
        pace = .25

    return pace

def change_rations():
    rations = 1
    choice = display_menu(["Double rations", "Normal rations", "Half rations"], "How good would you like to eat?")
    if choice == 1:
        pace = 1
    elif choice == 2:
        pace = .5
    else:
        pace = .25
    return rations

def rest(health_value,food,day, rations, members):
    day = day
    food = food
    health_value = health_value
    x = getNumberInRange("How many days would you like to rest?",1,9)
    for i in range(x):
        day += 1
        food = eat(rations,food,members)
        health_value += random.randint(5,15)
    return health_value, food, day

def checkSupplys(food,bullets,oxen,inventory):
    totalWheels = 0
    totalAxels = 0
    totalTongues = 0
    totalTarps = 0

    for part in inventory[4]:
        if part == "Wagon Wheel":
            totalWheels += 1
        elif part == "Wagon Axel":
            totalAxels += 1
        elif part == "Wagon tongue":
            totalTongues += 1
        elif part == "Wagon Tarp":
            totalTarps += 1
    print(str.format("""
    you have the following
    {}yokes of oxen
    {}pounds of food
    {}sets of clothing
    {}boxes of ammo
    and the following wagon parts
    {}Wheels
    {}Axles
    {}Tongues
    {}Tarps
    """, oxen, food, inventory[2],bullets, totalWheels, totalAxels, totalTongues, totalTarps))


def hunt(food,bullets):
    number = random.randint(1,2)
    if number == 1:
        print("good Hunt")
        food += random.randint(25,100)
        bullets -= random.randint(10,30)
        return food,bullets
    else:
        print("bad hunt")
        bullets -= random.randint(10, 30)
        return food, bullets


def travel(day,month,rations,members,health_value,food,oxen,total_miles,pace):
    if oxen >= 1:
        day, month, date = cur_day(day, month)
        weather,weather_mod = get_weather()
        food = eat(rations,food,members)
        health,health_value,members,health_mod = get_health(health_value,members)
        miles_travled = todays_travel(weather_mod,health_mod,pace)
        total_miles = total_miles - miles_travled

        print(str.format("""
           .....                                        ..'..                              ..',,,'..
        ..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..
        ,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
        ;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
        ''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                              ........        ...............            ...
         +-----------------------------+
         |Date:{:_>24}|
         |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.
         |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.
         |Miles Travled:{:_>15}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.
         |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.
         |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.
         +-----------------------------+            ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'
                         ..                         .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,
                  .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'
                   .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.
                 .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.
                  ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.
                        .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.
                         .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.
                          .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.
                        .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.
        '..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
        ;;;;;;;;;;;;;;,;;:::;;;::;,,;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;
        ;;;;;;;;;;;;;;,;::::;;;:;;;;;;;:::;;;;;;;;;;;;;;;;;;;;;;;;;,;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,
        ;;;;;;;;;;;;;;;;;:::;;;::;;;;;;;::;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;
        """, date, weather, health, miles_travled, total_miles, food))
        return day, month, date,weather,weather_mod,food,health,health_value,members,health_mod,total_miles
    else:
        game_quit()











# miles_travled = 0
# weather ="good"
# health_value = 100
# health = "good"
# alive = True
# day = 0
# year = 2022
# date = str(3)+"/"+str(day)+"/"+str(year)
# members = ["eric","Bob","sean"]


# this will be where we build the game
def game():

    miles_travled = 0
    health_value = 100
    start_month = ""
    day = 0
    year = 2022
    inventory = []
    total_miles = 2170


    # Game code go's here
    title_screen()
    prof, money, diff = prof_selection()
    player_name,members = party_namming()
    start_month = start_month_selection()
    inventory,money = shop(money)
    month = start_month
    food = inventory[1]
    bullets = inventory[3]
    oxen = inventory[0]
    rations = 1
    pace = 1


    while miles_travled < total_miles and health_value > 0:
        choice = display_menu(
            ["Travel trail", "change pace", "change rations", "check supplys", "rest", "hunt", "trade"],
            "what would you like to do?")
        if choice == 1:
            day, month, date, weather, weather_mod, food, health, health_value, members, health_mod, total_miles = travel(day,month,rations,members,health_value,food,oxen,total_miles,pace)
        elif choice == 2:
            pace = change_pace()
        elif choice == 3:
            rations = change_rations()
        elif choice == 4:
            pass  # check supplys
        elif choice == 5:
            health_value, food, day = rest(health_value,food,day, rations, members)
        elif choice == 6:
            food = hunt(food,bullets)
        elif choice == 7:
            print("Work in progress")

    if health_value > 0:
        print("Congrats")
    if health_value <= 0:
        print("To many Cheese Burgers Huh")

