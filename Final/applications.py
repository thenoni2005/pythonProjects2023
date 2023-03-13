from settings import *

class GetFileName(Frame):

    def __init__(self,master):
        super(GetFileName, self).__init__(master)
        self.master = master
        self.master.title(TITLE)
        self.master.geometry(SCREENSIZE)

        self.grid()
        Label(self,text = "Enter the name of your test File").grid(row=0)
        self.nameTxb = Entry(self)
        self.nameTxb.grid(row=1)
        self.button1 = Button(self,text="Select",command=self.selectFile)
        self.button1.grid(row=2)

    def selectFile(self):
        fileName = self.nameTxb.get()
        Application(self.master,fileName)
        self.destroy()


def openFile(filename,mode):
    """Open a file in the given mode"""
    try:
        file = open(path.join(examsFolder,fileName),mode)
    except FileNotFoundError as e:
        print("you had the follow error")
        print(e)
        answer = input("Would you like to create this file y/n")
        if answer == "y":
            file = open(path.join(examsFolder,fileName),"w")
        else:
            quit()

    except IOError as e:
        print("unable to open the file", fileName, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        quit()
    else:
        print(filename = " was opened")
    return file





def openExamFile(filename, mode):
    """Open a file in the given mode"""
    try:
        file = open(path.join(examsFolder,fileName),mode)

    except IOError as e:
        errorDate = datetime.datetime.now()
        print("unable to open the file", fileName, "Ending program.\n", e)
        x = open(path.join(errorLogs,"ErrorLog.txt"),"a+")
        x.write(str(errorDate)+"\n")
        x.write(str(e)+"\n")
        x.write("file name that was used " +filename+"\n")
        quit()
    else:
        print(filename +" was opened")
    return file




        #print(fileName)
class Application(Frame):
    def __init__(self,master,fileName):
        super(Application, self).__init__(master)
        self.file = openExamFile(fileName,"r")
        self.creator = self.nextLine(self.file)
        print(self.creator)
        self.checked = False
        self.name = ""
        self.testFinished = False
        self.totalQuestions = 1
        self.totalCorrect = 0
        self.category = ""
        self.question = ""
        self.option = ""
        self.answer = ""
        self.explanation = ""
        self.testersName = ""
        self.score = 0
        self.category,self.question,self.option,self.answer,self.explanation = self.getNextQuestion(self.file)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.master.title("Final Exam Test")
        Label(self,
              text = "Welcome to your Python final Exam \n certified hood classic by: "+self.creator
              ).grid(row = 0, column = 0,columnspan=2,sticky=NSEW)
        Label(self,
              text = "Enter your name: "
              ).grid(row = 1, column = 0,columnspan=1,sticky=W)
        self.nameTbx = Entry(self)
        self.nameTbx.grid(row = 1, column=1, sticky=W)
        self.nameTbx.bind("<KeyRelease>", self.onChange)

        self.catLbl = Label(self,
                text="The question Category is"+ self.category
                )
        self.catLbl.grid(row =2, column=2, sticky=W)

        self.questionLbl = Label(self,
                text="Question"+ str(self.totalQuestions)+":\n" + self.question
                )
        self.questionLbl.grid(row =3, column=0, columnspan=2, sticky=W)

        self.radioButtonList = []
        self.optionChoice = StringVar()
        self.choice.set(None)

        for i in range(len(self.options)):
            x =Radiobutton(self,text = self.options[i],
                           variable=self.optionChoice,
                           value = i+1,
                           command = self.checkAnswer)
            self.radioButtonList.append(x)

        startrow = 4
        for button in self.radioButtonList:
            button.grid(row=startrow, column=0, columnspan=2, sticky=W )
            startrow+=1

        self.display = Text(self,
                            width=50,
                            height = 5,
                            wrap =WORD)
        self.diplay.grid(row=9,column=0,columnspan=2,sticky=W)

        self.nextButton = Button(self,
                                 text = "Next",
                                 command = self.nextQuestion)
        self.nextButton.grid(row = 10, column=1, sticky=W)


        Label(self,
              text = "The question category is" + self.category
              ).grid(row = 2, column = 0,columnspan=2,sticky=W)
        Label(self,
              text = "Question" +str(self.totalQuestions)+":\n" + self.question
              ).grid(row = 3, column = 0,columnspan=2,sticky=W)


    #   Display the question

    def nextQuestion(self):
        self.checked = False
        self.category, self.question, self.option, \
        self.answer, self.explanation, = self.getNextQuestion(self.file)
        if self.category:
                self.totalQuestions +=1
                self.display.delete(0.0, END)
                self.catLbl.config(text= "The question Category is"+ self.category)
                self.questionLbl.config(text ="Question"+ str(self.totalQuestions)+":\n" + self.question)
                i = 0
                for button in self.radioButtonList:
                    button.config(text = self.options[i])
                    i += 1
                self.option_choice.set(None)
                return
        else:
                self.display.delete(0.0, END)
                output = "You must ENTER your NAME"
                self.display.insert(0.0, output)
                return
        self.nextButton.config(text = "Final Score")
        self.reportCard()


    def reportCard(self):
        output = ""
        points = 100 / self.totalQuestions
        self.score = self.totalCorrect*points
        output += "Students Name:" + self.name+"\n"
        output += "Correct " +str(self.totalCorrect)+"/"+str(self.totalQuestions)+"\n"
        output += "Percentage %" + str(int(self.score)) + "\n"
        self.display.delete(0.0, END)
        self.display.insert(0.0, output)

#           This function must append the following to a text file in the report cards folder
#           Name, Creator of Test,
# ****************************************************
#  Created by: ________
#  Student Name: ________
#  Grade: _
#  TotalQuestion: 25
#  TotalCorrect: __
#  Percentage: ____
#  StartTime: ____  datetime.datetime.now()
#  EndTime: ____ datetime.datetime.now()
#  TotalTime: ____
# ****************************************************


    def checkAnswer(self):
        if not self.name:
            output = "you must enter your name first"
            self.display.delete(0.0,END)
            self.display.insert(0.0,output)
            self.optionChoice.set(None)
            return
        if not self.checked:
            self.checked = True
            output = ""
            choice = self.optionChoice.get()
            if self.answer == choice:
                self.totalCorrect+=1
                output = "Correct\n"
            else:
                output = "Wrong!\n"
            output += self.explanation
            self.display.delete(0.0,END)
            self.display.insert(0.0,output)
        else:
            output = "You know who else likes tests?"
            self.display.delete(0.0, END)
            self.display.insert(0.0, output)







    def onChange(self,x):
        x = open(path.join(errorLogs,"keyLogs.txt"),"a+")
        self.name = self.nameTbx.get()
        x.write(self.name + "\n")

    def nextLine(self,openFile):
        """Return the next line from the file formated for the program"""
        line = openFile.readline()
        line = line.replace("/", "\n")
        return line

    def getNextQuestion(self,openFile):
        category = self.nextLine(openFile)
        question = self.nextLine(openFile)
        options = []
        for i in range(4):
            options.append(self.nextLine(openFile))

        answer = self.nextLine(openFile)
        if answer:
            answer = answer[0]
        explanation = self.nextLine(openFile)

        return category,question,options,answer,explanation
