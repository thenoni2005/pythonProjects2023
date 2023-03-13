from scripts.settings import *


class Player(pg.sprite.Sprite):

    def __init__(self,game, x , y, imageDir, colorKey):
        super(Player, self).__init__()

        self.image = self.getImage(imageDir)
        self.image.set_colorkey(colorKey)
        self.rect = self.image.get_rect()
        self.game = game
        #self.image = pg.Surface((50,50))
        #self.image.fill(color)
        #self.rect = self.image.get_rect()
        # MOVEMENT
        self.rect.center = (x,y)
        #CHANGE 0 TO MAKE A QUICK CHANGE IN MOVEMENT
        self.moveX = 5
        self.moveY = 3
        self.leftclick = False

        self.addToGroups()


    def addToGroups(self):
        self.game.allSprites.add(self)
        self.game.playerGroup.add(self)

    def getImage(self,imageDir):
        self.image = pg.image.load(imageDir).convert()
        self.image = pg.transform.scale(self.image,(70,70))
        return self.image


    def update(self):

        #mousePosition = pg.mouse.get_pos()
        #mouseX = mousePosition[0]
        #mouseY = mousePosition[1]
        #self.rect.centerx = mouseX
        #self.rect.centery = mouseY

        self.rect.center = pg.mouse.get_pos()
        self.leftclick = pg.mouse.get_pressed()[0]



        # SCREEN WRAPPING
        # if not solidBounds:
        #     if self.rect.left > WIDTH:
        #         self.rect.right = 0
        #
        #     elif self.rect.right < 0:
        #         self.rect.left = WIDTH
        #
        #     if self.rect.top > HEIGHT:
        #         self.rect.bottom = 0
        #
        #     elif self.rect.bottom < 0:
        #         self.rect.top = HEIGHT
        # else:
        #     if self.rect.left < 0:
        #         self.rect.left = 0
        #
        #     elif self.rect.right > WIDTH:
        #         self.rect.right = WIDTH
        #
        #     if self.rect.top < 0:
        #         self.rect.top = 0
        #
        #     elif self.rect.bottom > HEIGHT:
        #         self.rect.bottom = HEIGHT



