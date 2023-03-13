import pygame

from Settings import *
from gameObjects import *
from xboxLive import controller

def drawText(screen, text, size, x, y):
    fontName = pygame.font.match_font("papyrus")
    font = pg.font.Font(fontName, size)
    textSprite = font.render(text, True, cream)
    textRect = textSprite.get_rect()
    textRect.midtop = (x.y)
    screen.blit(textSprite, textRect)

class Game():

    def __init__(self):

        self.playing = True
        self.level = 1
        self.gameWindow = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()

        self.chestImg = GameObject(WIDTH / 2 - tileSize / 2, tileSize / 3, tileSize, tileSize, chestImageLocation)
        self.backgroundImg = GameObject(0,0,WIDTH,HEIGHT,bgImageLocation)
        self.player = Player(playerStartPositionX,playerStartPositionY,tileSize,tileSize,playerImg,playerSpeed)
        self.enemiesList = []
        self.spawnEnemy(self.level)
        self.hats = []
        self.resetLevel()
        self.hasOneUp = False
        if self.hasOneUp:
            self.oneUpX = 1000
            self.oneUpY = 0
            self.oneUpX = random.randint(0 + tileSize, WIDTH - tileSize)
            self.oneUpY = random.randint(0 + tileSize, HEIGHT - tileSize)


        self.extraLife = GameObject(self.oneUpX, self.oneUpY, tileSize, tileSize, extraLifeImg)

    def spawnEnemy(self,num):
        start = 0

        for i in range (num):

            enemyX = random.randint(0,WIDTH-tileSize)
            start += 105
            enemyY = start
            flip = random.choice(("h","t"))
            speed = random.randint(8,15)
            if flip == "t":
                speed *= -1
            enemy = Enemy(enemyX,enemyY, tileSize, tileSize, enemyImg,speed)
            self.enemiesList.append(enemy)
            if start > 760:
                start = 0

    def startGameLoop(self):
        while self.playing:
            # Tick Clock
            self.clock.tick(fps)
            # get input
            self.getInputs()
            # update
            self.update()
            # draw
            self.draw()



    def getInputs(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.playing = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_w or event.key == pg.K_UP:
                    self.player.setMoveDirection(0, -1)
                if event.key == pg.K_s or event.key == pg.K_DOWN:
                    self.player.setMoveDirection(0, 1)
                if event.key == pg.K_a or event.key == pg.K_LEFT:
                    self.player.setMoveDirection(-1, 0)
                if event.key == pg.K_d or event.key == pg.K_RIGHT:
                    self.player.setMoveDirection(1, 0)
                if event.key == pg.K_LSHIFT:
                    self.player.speed *= sprintMod

            elif event.type == pg.KEYUP:
                if event.key == pg.K_w or event.key == pg.K_UP or event.key == pg.K_s or\
                        event.key == pg.K_DOWN or event.key == pg.K_a or event.key == pg.K_LEFT or\
                        event.key == pg.K_d or event.key == pg.K_RIGHT:
                    self.player.setMoveDirection(0, 0)
                if event.type == pg.K_LSHIFT:
                    self.player.speed /= sprintMod
#SPEED CONSTANTLY INCREASES



    def update(self):
        if self.player.y > 0+tileSize or self.player.y < HEIGHT-tileSize:
            self.player.move()
        else: self.player.setMoveDirection(0)
        self.hats = controller.get_numhats()

        self.player.move()
        for enemy in self.enemiesList:
            enemy.move(WIDTH)


        if (self.detectCollisions(self.player, self.chestImg)):
            print("Player has won")
            self.player.collect()
            self.chestImg.collect()

        if self.detectCollisions(self.player,self.extraLife):
            print("Is this working?")
            self.extraLife.x += 1000
            self.player.lives += 1


        for enemy in self.enemiesList:
            if self.detectCollisions(self.player, self.enemy):
                self.player.die()

                if self.player.lives > 0:
                    self.resetLevel()
                else:
                    self.playing = False

        if self.player.collected and self.player.y > HEIGHT - 75:
            print("Boo, Haha jk you won baeb")
            self.nextLevel()

    def draw(self):
        self.gameWindow.fill(steelBlue)
        self.gameWindow.blit(self.backgroundImg.image,(self.backgroundImg.x,self.backgroundImg.y))
        self.gameWindow.blit(self.chestImg.image,(self.chestImg.x,self.chestImg.y))
        self.gameWindow.blit(self.player.image,(self.player.x,self.player.y))
        self.gameWindow.blit(self.extraLife.image,(self.extraLife.x, self.player.y))
        for enemy in self.enemiesList:
            self.gameWindow.blit(enemy.image,(enemy.x,enemy.y))
        pg.display.update()

    def detectCollisions(self, obj1, obj2):
# check if im colliding in the x direction
        if obj1.x > (obj2.x + obj2.width):
            return False
        elif (obj1.x + obj1.width) < obj2.x:
            return False
# check if im colliding in the x direction
        if obj1.y > (obj2.y + obj2.width):
            return False
        elif (obj1.y + obj1.width) < obj2.y:
            return False

        return True

    def showStart(self):
        self.gameWindow.fill(steelBlue)
        self.gameWindow.blit(self.backgroundImg.image,(self.backgroundImg.x,self.backgroundImg.y))
        self.gameWindow.blit(self.chestImg.image,(self.chestImg.x,self.chestImg.y))
        self.gameWindow.blit(self.player.image,(self.player.x,self.player.y))
        enemy = Enemy(WIDTH/2, HEIGHT/2, tileSize, tileSize, enemyImg, 0)
        self.gameWindow.blit(enemy.image, (enemy.x, enemy.y))

        drawText(self.gameWindow, TITLE, 80, WIDTH/2, HEIGHT/4, cream)

        drawText(self.gameWindow, TITLE, "Press A or enter to play", 50, WIDTH/2, HEIGHT -250, white)

        pg.display.flip()


        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        return "end"
            buttonInputs = self.xboxController.getButtons()
            a = buttonInputs.get("CONT_A")
            if a > 0:
                waiting = False
            start = buttonInputs.get("CONT_START")
            if a > 0:
                return "end"




    def showOver(self):
        self.gameWindow.fill(black)
        drawText(self.gameWindow,"You Lose, Boo!", 80, WIDTH/2, HEIGHT/4, red)
        drawText(self.gameWindow, TITLE, "Press A or enter to play", 50, WIDTH/2, HEIGHT-250, white)
        drawText(self.gameWindow, TITLE, "Press ESCAPE to QUIT", 50, WIDTH/2, HEIGHT-200, white)

        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RETURN:
                        waiting = False
                    if event.key == pg.K_ESCAPE:
                        return "end"
            buttonInputs = self.XboxController.getButtons()
            a = buttonInputs.get("CONT_A")
            if a > 0:
                waiting = False
            start = buttonInputs.get("CONT_START")
            if start > 0:
                return "end"

    def nextLevel(self):
        self.hasOneUp = random.choice([True,False,False])
        self.level += 1
        self.player.collected = False
        self.resetLevel()
        self.enemiesList = []
        self.spawnEnemy(self.level)
        if self.hasOneUp:

            self.oneUpX = random.randint(0 + tileSize, WIDTH - tileSize)
            self.oneUpY = random.randint(0 + tileSize, HEIGHT - tileSize)
        else:
            self.oneUpX = 1000
            self.oneUpY = 0
        self.extraLife.x = self.oneUpX
        self.extraLife.y = self.oneUpY


    def resetLevel(self):
        self.goal.reset()
        self.player.reset()


