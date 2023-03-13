import pygame as pg


class Controller():


   def __init__(self, cont_number=0):
       self.deadZone = .04

       try:
           self.controller = pg.joystick.Joystick(cont_number)
           self.controller.init()

           try:
               contId = self.controller.get_instance_id()
           except AttributeError:
               contId = self.controller.get_id()
       except IOError:
           print("no controller connected")


   def getDpad(self):
       dpad = self.controller.get_hat(0)
       x = dpad[0]
       y = dpad[1] * -1
       # set up key value pairs
       dpadDict = {"D_X": x, "D_Y": y}
       return dpadDict


   def getButtns(self):
       # get values
       aButton = self.controller.get_button(0)
       bButton = self.controller.get_button(1)
       xButton = self.controller.get_button(2)
       yButton = self.controller.get_button(3)
       lbButton = self.controller.get_button(4)
       rbButton = self.controller.get_button(5)
       startButton = self.controller.get_button(7)
       backButton = self.controller.get_button(6)
       xboxButton = self.controller.get_button(10)
       ljButton = self.controller.get_button(8)
       rjButton = self.controller.get_button(9)
       # set up key value paiB
       buttonsDict = {"CONT_A": aButton, "CONT_B": bButton, "CONT_X": xButton, "CONT_Y": yButton,
                       "CONT_LB": lbButton, "CONT_RB": rbButton, "CONT_START": startButton, "CONT_BACK": backButton,
                       "CONT_LJ": ljButton, "CONT_RJ": rjButton, "CONT_XBOX": xboxButton, }
       return buttonsDict


   def get_axes(self):
       # get values
       leftY = self.controller.get_axis(1)
       leftX = self.controller.get_axis(0)
       rightY = self.controller.get_axis(4)
       rightX = self.controller.get_axis(3)
       leftTrig = self.controller.get_axis(2)
       rightTrig = self.controller.get_axis(5)

       # clean up drift
       if leftX < self.deadZone and leftX > -self.deadZone:
           leftX = 0
       if leftY < self.deadZone and leftY > -self.deadZone:
           leftY = 0
       if rightX < self.deadZone and rightX > -self.deadZone:
           rightX = 0
       if rightY < self.deadZone and rightY > -self.deadZone:
           rightY = 0



       # set up key value pairs
       axisDict = {"LJOY_Y": leftY, "LJOY_X": leftX, "RJOY_Y": rightY, "RJOY_X": rightX, "LTRIG": leftTrig,
                    "RTRIG": rightTrig, }

       return axisDict

