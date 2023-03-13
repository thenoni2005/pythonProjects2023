from Settings import *

class GameObject():
    def __init__(self,x,y,width,height,imagePath):

        image = pg.image.load(imagePath)
        self.startX = x
        self.startY = y
        self.x = self.startX
        self.y = self.startY
        self.image = pg.transform.scale(image,(width,height))
        self.width = width
        self.height = height

        self.x = x
        self.y = y

    def collect(self):
        self.y -=100
    def reset(self):
        self.x = self.startX
        self.y = self.startY

class Player(GameObject):

    def __init__(self,x,y,width,height,imagePath,speed):
        super(Player, self).__init__(x,y,width,height,imagePath)
        self.speed = speed
        self.lives = 3
        self.sprintMod = sprintMod
        self.playerDirectionX = 0
        self.playerDirectionY = 0
        self.collected = False

    def move(self):
        if self.y < 0:
            self.y = 0
            return
        if self.y > HEIGHT-tileSize:
            self.y = HEIGHT-tileSize
            return
        self.y += (self.playerDirectionY * self.speed)

        if self.x < 0:
            self.x = 0
            return
        if self.x > WIDTH-tileSize:
            self.x = WIDTH-tileSize
            return
        self.x += (self.playerDirectionX * self.speed)

    #setter method
    def setMoveDirection(self,x,y):
        self.playerDirectionX = x
        self.playerDirectionY = y
        print(self.y)

    def collect(self):
        self.collected = True


    def die(self):

        self.x += 500
        self.lives -= 1
        self.collected = False
        print(self.lives)






class Enemy(GameObject):

    def __init__(self,x,y,width,height,imagePath,speed):
        super().__init__(x,y,width,height,imagePath)
        self.speed = speed

    def move(self,maxWidth):
        if self.x <= 0:
            self.speed = abs(self.speed)
        elif self.x > maxWidth - self.width:
            self.speed = -self.speed
        self.x += self.speed


