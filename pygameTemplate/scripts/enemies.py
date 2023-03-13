from scripts.settings import *
from scripts.player import *

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
