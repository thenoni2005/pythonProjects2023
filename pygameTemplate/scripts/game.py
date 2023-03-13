from scripts.settings import *
from scripts.player import *
from scripts.enemies import *


class Game(object):


    def __init__(self):

        self.playing = True
        pg.init()
        pg.mixer.init()  # if you are using ANY online editors you NEED to take this out


        # set up game screen
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        #pg.display.set_icon()# come back to later#
        self.clock = pg.time.Clock()
        # create sprite groups
        self.allSprites = pg.sprite.Group()
        self.enemyGroup = pg.sprite.Group()
        self.playerGroup = pg.sprite.Group()
        pg.mouse.set_visible(False)
        # create player objects
        #SPAWN AND COLOR
        self.playerOne = Player(self,200,75, playerImageLocation, BLACK)
        for i in range(6):
            Enemy(self,random.randint(0+Enemy.width,WIDTH-Enemy.width),random.randint(0+Enemy.height,HEIGHT-Enemy.height),enemyImageLocation,BLACK)



        self.playerOne.moveX *= -1

        # create enemy objects
        self.enemyOne = Enemy(self,WIDTH/2, HEIGHT/2, enemyImageLocation, BLACK)


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

     #   hits = pg.sprite.groupcollide(self.playerGroup,self.enemyGroup,True,False)
      #  if hits:
    #        for hit in hits:
   #             if self:
            #self.playing = False


        #hits = pg.sprite.groupcollide(self.playerGroup,self.enemyGroup,True,True)


    def updateAll(self):
        self.allSprites.update()


    def drawEverything(self):
        self.screen.fill(DEFAULT_COLORS)
        self.allSprites.draw(self.screen)


        # must be in the last line
        pg.display.flip()



    def startScreen(self):

        pass


    def endScreen(self):

        pass

