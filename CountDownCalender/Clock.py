import datetime
import random

from settings import *


class Application(Frame):
    date = "12/15/2022"



    def initUI(self):
        self.event = "????????"

        self.holidayIndex = 0
        self.imageIndex = 0
        img = PhotoImage(file = path.join(imgFolderList[self.holidayIndex],imgLists[self.holidayIndex][self.imageIndex]))
        self.bg = Label(self,image = img)
        self.bg.image = img
        self.bg.place(x=0,y=0)


        self.eventSelector = ttk.Combobox(self,textvariable="")
        self.eventSelector["values"] = ("Birthday","FourthOfJuly","Christmas","NewYears")
        self.eventSelector["state"] = "readonly"
        self.eventSelector.bind("<<ComboboxSelected>>",self.selectDate)
        self.eventSelector.place(x=1750,y=975)

        self.DefaultMonth = IntVar()
        self.dayDefaultVar = IntVar()
        self.DefaultYear = IntVar()

        self.DefaultMonth.set(datetime.datetime.now().month)
        self.dayDefaultVar.set(datetime.datetime.now().day)
        currentYear = datetime.datetime.now().year
        self.DefaultYear = currentYear



        self.moSpiner = Spinbox(self,from_=1,to=12,width = 5,textvariable=self.DefaultMonth)
        self.moSpiner.place(x=1650,y=1000)
        daysInMonth = 31
        x = self.moSpiner.get()
        if x in [4,6,9,11]:
            daysInMonth = 30
        elif  x == 2:
            daysInMonth = 28
        else:
            daysInMonth = 31



        self.daySpiner = Spinbox(self, from_=1, to=daysInMonth, width=5, textvariable=self.dayDefaultVar)
        self.daySpiner.place(x=1700, y=1000)

        self.yearSpiner = Spinbox(self, from_=currentYear, to=currentYear +5, width=8,textvariable=self.DefaultYear)
        self.yearSpiner.place(x=1750, y=1000)

        self.eventLbl = Label(self,text = "Time Until" + self.event,fg="#00873E", font=("helvetica", 58))
        self.eventLbl.place(x = 101, y = 101)
        Label(self,text = "Days",fg="#00873E", font=("helvetica", 58)).place(x=201,y=201)
        Label(self,text = "Hours",fg="#00873E", font=("helvetica", 58)).place(x=411,y=201)
        Label(self,text = "Minutes",fg="#00873E", font=("helvetica", 58)).place(x=651,y=201)
        Label(self,text = "Seconds",fg="#00873E", font=("helvetica", 58)).place(x=951,y=201)


        self.daysLbl = Label(self,text = "0000",fg="#00873E", font=("helvetica", 58))
        self.daysLbl.place(x=201,y=301)
        self.hoursLbl = Label(self, text="00", fg="#00873E", font=("helvetica", 58))
        self.hoursLbl.place(x=511, y=301)
        self.minLbl = Label(self, text="00", fg="#00873E", font=("helvetica", 58))
        self.minLbl.place(x=751, y=301)
        self.secLbl = Label(self, text="00", fg="#00873E", font=("helvetica", 58))
        self.secLbl.place(x=1051, y=301)
        self.date = self.setDate()


        self.changeImageBtn = Button(self,text = "Happiness",command = self.changePic)
        self.changeImageBtn.place(x=WIDTH/2,y=HEIGHT/2)

    def selectDate(self, x):
        print("testing")
        curMonth = datetime.datetime.now().month
        curDay = datetime.datetime.now().day
        curYear = datetime.datetime.now().year
        curDate = datetime.datetime.now()

        self.x = self.eventSelector.get()

        if (self.x == "Christmas"):
            self.holidayIndex = 2
            day = 25
            month = 12
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1

            self.dayDefaultVar.set(day)
            self.DefaultMonth.set(month)
            return True

        elif self.x == "NewYears":
            self.holidayIndex = 3
            day = 31
            month = 4
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.dayDefaultVar.set(day)
            self.DefaultMonth.set(month)
            return True
        elif self.x == "FourthOfJuly":
            self.holidayIndex = 1
            return True
        elif self.x == "Birthday":
            self.holidayIndex = 0

            return True
        else:
            return False
    # had 2 update functions
    def update(self):

        days = StringVar()
        hours = StringVar()
        min = StringVar()
        sec = StringVar()

        days = self.timeUntil(self.date).days
        totalSeconds = self.timeUntil(self.date).seconds

        total_min = totalSeconds//60
        total_hours = total_min//60

        cur_sec = totalSeconds % 60
        cur_min = total_min % 60
        cur_hour = total_hours % 24

        hours = cur_sec
        min = cur_min
        sec = cur_hour

        self.daysLbl.config(text = days)
        self.hoursLbl.config(text = hours)
        self.minLbl.config(text = min)
        self.secLbl.config(text = sec)

        self.master.after(1,self.update)

    def setDays(self):
        dayInMonth = 31
        x = self.moSpiner.get()
        if x in [4,6,9,11]:
            daysInMonth = 30
        elif x == 2:
            daysInMonth = 28
        else:
            daysInMonth = 31

        self.daySpiner.config["to"] = daysInMonth


    def setDate(self):

        month = self.moSpiner.get()
        day = self.daySpiner.get()
        year = self.yearSpiner.get()
        return str(month)+"/"+str(day)+"/"+str(year)



    def timeUntil(self,date):
        date = datetime.datetime.strptime(date, "%m/%d/%Y")
        now = datetime.datetime.now()
        if date > now:
            timeUntil = date - now
            return timeUntil
        else:
            return now - now

    def changePic(self):
        ok = self.selectDate(self)
        if ok:
            self.imageIndex = random.randint(0, len(imgLists[self.holidayIndex])-1)
            img = PhotoImage(file = path.join(imgFolderList[self.holidayIndex],imgLists[self.holidayIndex][self.imageIndex]))
            self.bg.configure (image=img)
            self.bg.image = img
        self.date = self.setDate()

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.master.title(title)
        self.master.geometry(SCREEN_SIZE)
        self.initUI()
        self.pack(fill=BOTH, expand=1)



