import pygame as pg
import random
import os.path

#debug = True

# COLOR RGB BW
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLDENYELLOW = (255, 255, 0)


# GAME TITLE
TITLE = "Playing minecraft in a cave looking for diamonds"


# SCREEN/WINDOW
WIDTH = 600
HEIGHT = 900
DEFAULT_COLORS = BLACK

fps = 40

# FILE LOCATIONS
gameFolder = os.path.dirname(__file__)
gameFolder = gameFolder.replace("\scripts","")
spritesFolder = os.path.join(gameFolder, "sprites")
playerFolder = os.path.join(spritesFolder,"playerSprites")
enemyFolder = os.path.join(spritesFolder,"enemySprites")
backgroundFolder = os.path.join(spritesFolder,"background")
explosionFolder = os.path.join(spritesFolder,"explosion")
bulletFolder = os.path.join(playerFolder,"bullets")
powerUpFolder = os.path.join(playerFolder,"powerUp")


bgImg = "Space_BG_02.png"

# CAMERA SETTINGS



# PLAYER SETTINGS GO HERE
solidBounds = True
moveSpeed = 10
stopSpeed = 0


playerImageLocation = "playerSteve.png"
playerW = 50
playerH = 50

bulletImg = "Projectile.png"
bulletW = 10
bulletH = 20
# ENEMY SETTINGS GO HERE


