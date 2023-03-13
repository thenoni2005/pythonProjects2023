# ANTHONY TRUJILLO#
# 9/22/2022#
# MADLIB3#

# imports#


# globals#
OGTEXT3 = """
the one piece, the one piece is real
can we get much higher? So high
Oh, oh, oh
Oh, oh, oh, oh
Oh, oh
Can we get much higher? So high
Oh, oh, oh
Oh, oh, oh, oh
Oh, oh
Can we get much higher? So high
Oh, oh, oh
Oh, oh, oh, oh
Oh, oh
Can we get much higher? So high
Oh, oh, oh
Oh, oh, oh, oh
Oh, oh
"""

# functions#


# main#
def main():
    text3 = OGTEXT3

    words =["higher","oh","piece","one"]
    i = 0
    for word in words:
        text3 = text3.replace(word,"({"+str(i)+"})")
        i+=1
    vars = []
    for i in range(len(words)):
        x = input("Give me a word to Replace "+words[i])
        vars.append(x)

    text3 = str.format(text3,vars[0],vars[1],vars[2],vars[3])

    print(text3)

main()