from scripts.settings import *
from scripts.player import *

class Mob(pg.sprite.Sprite):
    def __init__(self, game, img, color):
        super(Mob, self).__init__()
        self.game = game
        self.imageOriginal = img
        self.image = self.imageOriginal.copy()
        self.image.set_colorkey(color)
        #self.image = pg.Surface((50, 50))
        #self.image.fill(RED)
        self.rect = self.image.get_rect()
        #self.radius = int(self.rect.WIDTH/2)
        #for debug
        #if debugging:
            #pg.draw.circle(self.image,RED,self.rect.center,self.radius)

        # MOVEMENT
        self.respawn()
        self.addToGroups()


    def addToGroups(self):
        self.game.allSprites.add(self)
        self.game.enemyGroup.add(self)



    def update(self):
        self.rect.centerx += self.moveX
        self.rect.centery += self.moveY
        if self.rect.y > HEIGHT + 100:
            self.respawn()
        if self.rect.x > WIDTH + 50 or self.rect.x < -50:
            self.respawn()
        self.rotate()

    def respawn(self):
        self.rect.center = (random.randint(0+self.rect.width, WIDTH - self.rect.width), random.randint(-250,-50))
        self.moveX = random.randint(-2,2)
        self.moveY = random.randint(3,11)
        self.rot = 0
        self.rotSpeed = random.randint(-8,8)
        self.lastUpdate = pg.time.get_ticks()


    def rotate(self):
        now = pg.time.get_ticks()
        if now - self.lastUpdate > fps:
            self.lastUpdate = now
            self.rot = (self.rot + self.rotSpeed)%360
            newImage = pg.transform.rotate(self.imageOriginal, self.rot)
            oldCenter = self.rect.center
            self.image = newImage
            self.rect = self.image.get_rect()
            self.rect.center = oldCenter





class Enemy(Player):
    width = 50
    height = 50
    def __init__(self,game,x,y,imageDir, colorKey):
        super(Enemy, self).__init__(game,x,y,imageDir,colorKey)

    def addToGroups(self):
        self.game.allSprites.add(self)
        self.game.enemyGroup.add(self)

    def update(self):
        self.rect.center = (self.rect.centerx + self.moveX, self.rect.centery + self.moveY)
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.moveX *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.moveY *= -1
