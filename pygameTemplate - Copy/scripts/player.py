from scripts.settings import *


class Player(pg.sprite.Sprite):

    def __init__(self,game, x , y, img, color):
        super(Player, self).__init__()
        #self.rect = self.image.get_rect()
        self.game = game
        #self.image = pg.Surface((50,50))
        #self.image.fill(color)
        self.image = img
        self.image.set_colorkey(color)
        self.rect = self.image.get_rect()
        # MOVEMENT
        self.rect.center = (x,y)
        #CHANGE 0 TO MAKE A QUICK CHANGE IN MOVEMENT
        self.moveX = 0
        #self.moveY = 3
        #self.leftclick = False
        self.addToGroups()
        self.canShoot = True
        #self.radius = int(self.rect.WIDTH/2)
        #for debug
        #if debugging:
            #pg.draw.circle(self.image,RED,self.rect.center,self.radius)pro

    def addToGroups(self):
        self.game.allSprites.add(self)
        self.game.playerGroup.add(self)

   #def getImage(self,imageDir):
        #self.image = pg.image.load(imageDir).convert()
        #self.image = pg.transform.scale(self.image,(70,70))
        #return self.image

    def setMoveX(self, value):
        self.moveX = value


    def update(self):
        self.moveX = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT] or keystate[pg.K_a]:
            self.setMoveX(-moveSpeed)
        if keystate[pg.K_RIGHT] or keystate[pg.K_d]:
            self.setMoveX(moveSpeed)
        if keystate[pg.K_SPACE]:
            if self.canShoot:
                self.shoot()
        if keystate[pg.K_SPACE] == False:
            self.canShoot = True



        # SCREEN WRAPPING
        if not solidBounds:
            if self.rect.left > WIDTH:
                self.rect.right = 0

            elif self.rect.right < 0:
                self.rect.left = WIDTH

            if self.rect.top > HEIGHT:
                self.rect.bottom = 0

            elif self.rect.bottom < 0:
                self.rect.top = HEIGHT
        else:
            if self.rect.left < 0:
                self.rect.left = 0

            elif self.rect.right > WIDTH:
                self.rect.right = WIDTH

            if self.rect.top < 0:
                self.rect.top = 0

            elif self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT

        self.rect.x += self.moveX


    def shoot(self):
        self.canShoot = False
        Bullet(self.game,self.rect.centerx,self.rect.top-2,self.game.bulletImg)

class Bullet(pg.sprite.Sprite):
    def __init__(self, game, x, y, image):
        super(Bullet, self).__init__()
        self.game = game
        self.image = pg.Surface((5, 10))
        self.image.fill(GOLDENYELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.moveY = -10
        self.addToGroups()

    def addToGroups(self):
        self.game.allSprites.add(self)
        self.game.bulletGroup.add(self)

    def update(self):
        self.rect.y += self.moveY
        if self.rect.bottom < 0:
            self.kill()


