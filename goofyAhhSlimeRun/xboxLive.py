import pygame as pg
# line 18

BLACK = pg.Color("black")
WHITE = pg.Color("white")


class TextPrint(object):
    def __init__(self, fontSize):
        self.fontSize = fontSize
        self.x = ""
        self.y = ""
        self.lineHeight = ""
        self.font = pg.font.Font(None, fontSize)
        self.reset()

    def tprint(self,screen,text):
        textBitMap = self.font.render(text, True, BLACK)
        screen.blit(textBitMap, (self.x, self.y))
        # Comment this out for text not to move
        self.y += self.lineHeight

    def reset(self):
        self.x = 15
        self.y = 15
        self.lineHeight = self.fontSize-5

    def indent(self):
        self.x += 10

    def unIndent(self):
        self.x -= 10




pg.init()
screen = pg.display.set_mode((500,900))
pg.display.set_caption("XBOX LIVE")

running = True

clock = pg.time.Clock()
fps = 40
text = TextPrint(25)
screen.fill(WHITE)
pg.joystick.init()
controllerList = ""

while running:

    # Tick Clock
    clock.tick(fps)

    # Get Input


    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.JOYBUTTONDOWN:
            print("Pressed a button")
        elif event.type == pg.JOYBUTTONUP:
            print("Released a button")

    screen.fill(WHITE)
    text.reset()

    joyStickCount = pg.joystick.get_count()
    text.tprint(screen,"number of joysticks {}".format(joyStickCount))
    text.indent()

    for i in range(joyStickCount):
        controller = pg.joystick.Joystick(i)
        controller.init()

        try:
            controllerId = controller.get_instance_id()
        except AttributeError:
            controllerId = controller.get_id()
        text.tprint(screen, "Controller {}".format(controllerId))
        text.indent()

        controllerName = controller.get_name()
        text.tprint(screen, "controller name {}".format(controllerName))

        try:
            guid = controller.get_guid()
        except AttributeError:
            pass
        else:
            text.tprint(screen, "GUID {}".format(guid))

        axes = controller.get_numaxes()
        text.tprint(screen,"number of axes {}".format(axes))
        text.indent()
        for i in range(axes):
            axis = controller.get_axis(i)
            text.tprint(screen, "axis {} value {:>6.3f}".format(i, axis))
        text.unIndent()
        buttons = controller.get_numbuttons()
        text.tprint(screen, "number of buttons {}".format(buttons))
        text.indent()


        for i in range(buttons):
            button = controller.get_button(i)
            text.tprint(screen, "Button {:>2} value: {}".format(i, button))
        text.unIndent()

        hats = controller.get_numhats()
        text.tprint(screen, "Number of hats: {}".format(hats))
        text.indent()

        for i in range(hats):
            hat = controller.get_hat(i)
            text.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
            text.indent()

    # Update
#0 A
#1 B
#2 X
#3 Y
#4 LB
#5 RB
#6 LMENU button
#7 RMENU button
#8 L3
#9 R3
# (0, 1) Forward
# (1, 0) Right
# (0 , -1) Down
# (-1, 0) Left

    # Draw
    text.reset()
    pg.display.flip()

pg.quit()
quit()