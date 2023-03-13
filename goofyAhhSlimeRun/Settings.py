import pygame as pg
import random
from XboxController import *

TITLE = "Go0Fy AhH SlimeRun"

#DISPLAY
WIDTH = 800
HEIGHT = 1000
fps = 40
tileSize = HEIGHT/20

#COLORS
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,225,0)
blue = (0,0,255)
cream = (164,143,94)
steelBlue = (70,130,180)

#SPRITES

bgImageLocation = "background.png"
chestImageLocation = "treasure.png"
playerImg = "player.png"
enemyImg = "enemy.png"
extraLifeImg = "heart_full_32x32.png"

#player
playerStartPositionX = WIDTH/2-tileSize/2
playerStartPositionY = HEIGHT-tileSize
playerSpeed = 4
sprintMod = 2
#monster
monsterSpeed = 4
