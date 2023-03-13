# Anthony. Trujillo
# 9/20/2022
# Mad Lib


# imports


# globals
ORIGINALTEXT ="""
Rise and (shine), Mister (Freeman). Rise and... (shine).   
Not that I... wish to imply (you) have been (sleeping) on the (job). No (one) is more (deserving) of a (rest), 
and all the (effort) in the (world) would have gone to (waste) until... well, 
(let's) just say (your) (hour) has... (come) again.
The (right) (man) in the wrong (place) can make all the (difference) in the (world).
So, wake up, Mister (Freeman). Wake up and... (*smell the ashes*)...

"""


# functions



# main



def main():
    shine = input("Give me a descriptive word")
    freeman = input("Give me a name")
    you = input("Give me a name")
    sleeping = input("Give me an action")
    job = input("Give me an activity")
    one = input("Give me a name")
    deserving = input("Give me a describing word")
    rest = input("Give me an action")
    effort = input("Give me a word")
    world = input("Give me a location")
    waste = input("Give me a location")
    lets = input("Give me a name")
    your = input("Give me a name")
    hour = input("Give me a descriptive word")
    come = input("Give me a descriptive word")
    right = input("Give me a word like right or wrong")
    man = input("Give me a name")
    place = input("Give me a location")
    difference = input("Give me a descriptive word")
    smell_the_ashes = input("Give me a sentence")


    text1 = """
.
Rise and ("""+shine+"""), Mister ("""+freeman+"""). Rise and... ("""+shine+""").
Not that I... wish to imply ("""+you+""") have been ("""+sleeping+""") on the ("""+job+"""). No ("""+one+""") is more ("""+deserving+""") of a ("""+rest+"""),
and all the ("""+effort+""") in the ("""+world+""") would have gone to ("""+waste+""") until... well,
("""+lets+""") just say ("""+your+""") ("""+hour+""") has... ("""+come+""") again.
The ("""+right+""") ("""+man+""") in the wrong ("""+place+""") can make all the ("""+difference+""") in the ("""+world+""").
So, wake up, Mister ("""+freeman+"""). Wake up and... ("""+smell_the_ashes+""")"""
main()

print(text1)

input()
