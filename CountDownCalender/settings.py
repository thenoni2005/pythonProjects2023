from tkinter import *
from tkinter import ttk
from os import path
import random
import datetime

HEIGHT = 1080
WIDTH = 1920

SCREEN_SIZE = str(WIDTH)+"x"+str(HEIGHT)

title = "Christmas CountDown"

LOCATION = path.dirname(__file__)
imageFolder = path.join(LOCATION, "PNG")
birthdayFolder = path.join(imageFolder,"Birthdays")
ChristmasFolder = path.join(imageFolder,"Christmas")
FourthOfJulyFolder = path.join(imageFolder,"FourthOfJuly")
NewYearsFolder = path.join(imageFolder,"NewYears")

christmasImageList = []
for i in range(5):
    christmasImageList.append(str.format("Christmas{}.png",i+1))


birthdayImageList = []
for i in range(1):
    birthdayImageList.append(str.format("birthday{}.png",i+1))

fourthOfJulyImageList = []
for i in range(1):
    fourthOfJulyImageList.append(str.format("FourthOfJuly{}.png",i+1))

newYearsImageList = []
for i in range(1):
    newYearsImageList.append(str.format("NewYears{}.png",i+1))

imgFolderList = [FourthOfJulyFolder,birthdayFolder,ChristmasFolder,NewYearsFolder]
imgLists = [fourthOfJulyImageList,birthdayImageList,christmasImageList ,newYearsImageList]



