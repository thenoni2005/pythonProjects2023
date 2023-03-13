from tkinter import *
import datetime
from os import path

HEIGHT = 420
WIDTH = 640
createApp = False

TITLE = "Term 2 Final Exam"

SCREENSIZE = str(HEIGHT)+"x"+str(WIDTH)

fileName = "Text.txt"

location = path.dirname(__file__)
examsFolder = path.join(location,"exams")
reportsFolder = path.join(location,"reports")
errorLogs = path.join(reportsFolder,"errorLogs")
reportCards = path.join(reportsFolder,"reportCards")

test = path.join(examsFolder,fileName)
