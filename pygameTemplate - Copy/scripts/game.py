from scripts.settings import *
from scripts.player import *
from scripts.enemies import *
from scripts.explosions import *


class Game(object):


    def __init__(self):

        self.playing = True
        pg.init()
        pg.mixer.init()
        # if you are using ANY online editors you NEED to take this out


        # set up game screen
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        #pg.display.set_icon()# come back to later#
        self.clock = pg.time.Clock()
        self.mobImg = []
        self.explosionAnimation = {}
        self.explosionAnimation["L"] = []
        self.explosionAnimation["S"] = []

        self.loadImgs()

        # create sprite groups
        self.allSprites = pg.sprite.Group()
        self.enemyGroup = pg.sprite.Group()
        self.playerGroup = pg.sprite.Group()
        self.bulletGroup = pg.sprite.Group()
        #pg.mouse.set_visible(False)
        # create player objects
        self.player = Player(self, WIDTH/2, HEIGHT - 50, self.playerImg, BLACK)
        #SPAWN AND COLOR
        #CREATE ENEMY
        for i in range(80):
            Mob(self,random.choice(self.mobImg),BLACK)

        exp = Explosion(self,(100,100),"L")


    def loadImgs(self):
        self.bgImg = pg.image.load(os.path.join(backgroundFolder,bgImg)).convert()
        self.bgImg = pg.transform.scale(self.bgImg,(WIDTH,HEIGHT))
        self.playerImg = pg.image.load(os.path.join(playerFolder,playerImageLocation)).convert()
        self.playerImg = pg.transform.scale(self.playerImg,(playerW,playerH))
        for i in range(4):
            z = pg.image.load(os.path.join(enemyFolder,str.format("enemy0{}.png",i)))
            z = pg.transform.scale(z,(50,50))
            self.mobImg.append(z)
        self.bulletImg = pg.image.load(os.path.join(bulletFolder,bulletImg))
        self.bulletImg = pg.transform.scale(self.bulletImg,(bulletW,bulletH))

        for i in range(9):
            filename = str.format("explosion.png", i)
            image = pg.image.load(os.path.join(explosionFolder,filename)).convert()
            image.set_colorkey(BLACK)
            imgL = pg.transform.scale(image, (75,75))
            imgS = pg.transform.scale(image, (75, 75))
            self.explosionAnimation["L"].append(imgL)
            self.explosionAnimation["S"].append(imgS)


    def gameLoop(self):
        while self.playing:

            # tick clock
            self.clock.tick(fps)
            # check for events
            self.checkEvents()
            # update all
            self.updateAll()
            # draw everything
            self.drawEverything()


    def checkEvents(self):
        for event in pg.event.get():
            # check if trying to close the window
            if event.type == pg.QUIT:
                self.playing = False




    def updateAll(self):
        self.allSprites.update()

        # This is the collision between player and mobs :D
        hits = pg.sprite.spritecollide(self.player, self.enemyGroup, False)
        if hits:
            # game over D:
            self.playing = False
        # check for collision between projectile and enemy
        hits = pg.sprite.groupcollide(self.enemyGroup, self.bulletGroup, True, True)
        if hits:
            for hit in hits:
                exp = Explosion(self, hit.rect.center, "S")

    def drawEverything(self):
        self.screen.fill(DEFAULT_COLORS)
        self.screen.blit(self.bgImg,self.bgImg.get_rect())
        self.allSprites.draw(self.screen)


        # must be in the last line
        pg.display.flip()



    def startScreen(self):

        pass


    def endScreen(self):

        pass

