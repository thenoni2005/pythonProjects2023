def writeQuestion(list, openFile, ):
    for i in list:
        openFile.write(i + "\n")


openFile = open("exams/Text.txt", "w")
openFile.write("Anthony Trujillo\n")

question1 = ["Functions",
             "What does a print statement do?",
             "Make pancakes",
             "Fry some eggs",
             "Make some bacon",
             "Display text in your parenthesis",
             "4",
             "Print statements do not make breakfast\n",]
question2 = ["Functions",
             "What kind of functions displays text?",
             "Else",
             "input",
             "if",
             "Print",
             "4",
             "Print statements display text\n",]
question3 = ["Functions",
             "What is boolean?",
             "Maybe or Maybe Not values",
             "Simple or Confused",
             "Bacon or Pancakes",
             "True or False values",
             "4",
             "Boolean hold true and false\n",]
question4 = ["Functions",
             "What do you import to use random",
             "import cheese",
             "import not random",
             "import selected values",
             "import random",
             "4",
             "To use random you must import random\n",]
question5 = ["Functions",
             "What do you import to use date and time",
             "watch",
             "fart",
             "history",
             "datetime",
             "4",
             "To use datetime you must import datetime\n",]
question6 = ["Functions",
             "What is the name of the programming language beginning with P",
             "Pancake",
             "Purple",
             "Phunky",
             "Python",
             "4",
             "Python is the only answer",]
question7 = ["Functions",
             "What do you import to use math",
             "math",
             "meth",
             "Heisenberg",
             "Jesse Pinkman",
             "4",
             "Explanation\n",]
question8 = ["Functions",
             "What is the second letter in the word python",
             "p",
             "n",
             "o",
             "y",
             "4",
             "The second letter in python is n",]
question9 = ["Functions",
             "What is the third letter in the word python",
             "p",
             "y",
             "o",
             "t",
             "4",
             "The third letter in python is t",]
question10 = ["Operators",
              "What are logical operators",
              "Hope",
              "Fear",
              "Joy",
              "AND,OR,NOT",
              "4",
              "Logical operators include AND,OR,NOT",]
question11 = ["Operators",
              "What are relational operators",
              "AND,OR,NOT",
              "Hope",
              "Joy",
              "==,! = ,>, >",
              "4",
              "Relational Operators are comparison operators",]
question12 = ["Operators",
              "What are arithmetic operators",
              "AND,OR,NOT",
              "Hope",
              "Joy",
              "+,-,/,%",
              "4",
              "Arithmetic Operators are mathematical operators",]
question13 = ["Operators",
              "How do you compare two values",
              "You add them",
              "You subtract them",
              "You divide them",
              "> , <",
              "4",
              "Relational Operators are comparison operators",]
question14 = ["Operators",
              "How do you compare two values",
              "You add them",
              "You subtract them",
              "You divide them",
              "> , <",
              "4",
              "Relational Operators are comparison operators",]
question15 = ["Operators",
              "How do you add two values",
              "You compare them",
              "You subtract them",
              "You divide them",
              "You add them",
              "4",
              "To add two values you simply add them",]
question16 = ["Operators",
              "How do you subtract two values",
              "You compare them",
              "You add them",
              "You divide them",
              "You subtract them",
              "4",
              "To subtract two values you simply subtract them",]
question17 = ["Operators",
              "How do you divide two values",
              "You compare them",
              "You add them",
              "You subtract them",
              "You divide them",
              "4",
              "To divide two values you simply divide them",]
question18 = ["Operators",
              "How do you slowly add one to your value",
              "You compare them",
              "You add them",
              "You subtract them",
              "+=",
              "4",
              "+= slowly adds one to your value in your function",]
question19 = ["Operators",
              "What does % do in python",
              "You compare them",
              "You add them",
              "You subtract them",
              "Give you the remainder",
              "4",
              "Gives you the remainder",]
question20 = ["Functions",
              "What does * do in python",
              "You compare them",
              "You add them",
              "You subtract them",
              "Multiplies your values",
              "4",
              "The star symbol is the multiplier symbol",]
question21 = ["Functions",
              "What does IF do in python",
              "You compare them",
              "You add them",
              "You subtract them",
              "Runs a function if a certain thing is true",
              "4",
              "If statements run when something is true",]
question22 = ["Functions",
              "What does AND do in python",
              "You compare them",
              "You add them",
              "You subtract them",
              "Runs a block of code if both statements are true",
              "4",
              "If statements run when something is true",]
question23 = ["Functions",
              "What does ELSE do in python",
              "You compare them",
              "You add them",
              "You subtract them",
              "Runs a block of code if given statements are false",
              "4",
              "If statements run when something is false",]
question24 = ["Functions",
              "What does () do in python",
              "You compare them",
              "You add them",
              "You subtract them",
              "Contains your code to separate it",
              "4",
              "If statements run when something is false",]
question25 = ["Functions",
              "What does [] do in python",
              "You compare them",
              "You add them",
              "You subtract them",
              "Creates a list",
              "4",
              "creates a list",]

questions = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12,question13,question14,question15,question16,question17,question18,question19,question20,question21,question22,question23,question24,question25]

for question in questions:
    writeQuestion(question,openFile)


# openFile = open("Text.txt","r")
# list = openFile.readlines()
# print(list)
#
# for i in range(len(list)):
#     list[i] = list[i].strip("\n")
#
# print(list)
# openFile.close()
#
# openFile = open("Text.txt","w")
# openFile.write("Anthony Trujillo python term 2 final Exam")
# openFile.write("Question Category")
# openFile.write("What is the Question to ask?")
# openFile.write("Option 1")
# openFile.write("Option 2")
# openFile.write("Option 3")
# openFile.write("Option 4")
# openFile.write("Answer")
# openFile.write("Explanation")
# for i in range(24):
#     openFile.write("""Category
# Question
# Option 1
# Option 2
# Option 3
# Option 4
# Answer
# Explanation
# """)
# openFile.close()
