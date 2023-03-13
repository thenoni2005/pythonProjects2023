from scripts.settings import *


class Explosion(pg.sprite.Sprite):
    def __init__(self, game, center, size):
        super(Explosion, self).__init__()
        self.size = size
        self.game = game
        self.frame = 0
        self.image = self.game.explosionAnimation[self.size][self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.lastUpdate = pg.time.get_ticks()
        self.frameRate = 30
        self.game.allSprites.add(self)

    def update(self):
        now = pg.time.get_ticks()
        if now - self.lastUpdate > self.frameRate:
            self.lastUpdate = now
            self.frame += 1
            if self.frame == len(self.game.explosionAnimation[self.size]):
                self.kill()
            else:
                oldCenter = self.rect.center
                self.image = self.game.explosionAnimation[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = oldCenter

