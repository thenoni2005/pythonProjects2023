class Person(object):
    peopleCount = 0
    languages = ["English","Spanish","Japanese","French","Chinese","Hindi"]
    def __init__(self,name,alive = True,happy = True,mad = False,eyeColor = "Brown",gender = "na",height = 0,weight = 0,age = 0,bloodtype = "O+",haircolor = "black",race = "na"):
        Person.peopleCount += 1
        self.name = name
        self.isAlive = alive
        self.happy = happy
        self.mad = mad
        self.spokenLanguage = ""
        self.eyeColor = eyeColor
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.bloodType = bloodtype
        self.allergies = []
        self.hairColor = haircolor
        self.race = race

    def speak(self,speech):
        print(speech)
    def walk(self):
        print("walking")
    def run(self):
        print("running")
    def die(self):
        self.isAlive = False
        Person.peopleCount -= 1

    def breath(self):
        pass
    def sleep(self):
        pass
    def eat(self):
        pass
    def jump(self):
        pass
    def grow(self,amount):
        self.height += amount
    def gainWeight(self,amount):
        self.weight += amount
    def loseWeight(self,amount):
        self.weight -= amount
    def __str__(self):
        dis = self.name + "\n"
        dis += str(self.height) + "Inches Tall\n"
        dis += str(self.weight) + "Pounds\n"
        dis += self.gender + "\n"
        dis += str(self.eyeColor) + "eyes\n"
        dis += str(self.hairColor) + "hair"
        return dis

