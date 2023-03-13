import pygame as pg
import random
import os.path


# COLOR RGB BW
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLDENYELLOW = (255, 255, 0)


# GAME TITLE
TITLE = "WIP"


# SCREEN/WINDOW
WIDTH = 1000
HEIGHT = 1000
DEFAULT_COLORS = BLACK

fps = 60

# FILE LOCATIONS
gameFolder = os.path.dirname(__file__)
gameFolder = gameFolder.replace("\scripts","")
spritesFolder = os.path.join(gameFolder, "sprites")
playerSprites = os.path.join(spritesFolder,"playerSprites")
enemySprites = os.path.join(spritesFolder,"enemySprites")

# CAMERA SETTINGS



# PLAYER SETTINGS GO HERE
solidBounds = False
bouncy = True

playerImageLocation = os.path.join(playerSprites,"enderPearl.png")



# ENEMY SETTINGS GO HERE

enemyImageLocation = os.path.join(enemySprites,"fireCharge.png")

