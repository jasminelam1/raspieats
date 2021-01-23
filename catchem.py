from sense_hat import SenseHat
from time import sleep
from random import choice, randint

sense = SenseHat()
sense.clear()

game_over = False

catcher_x = 0
berry_x = randint(0, 7)
berry_y = 0

score = 0

r = (255, 0, 0) #red
g = (0, 255, 0) #green
b = (0, 0, 255) #blue
k = (0, 0, 0) #blank
w = (255, 255, 255) #white
c = (0, 255, 255) #cyan
y = (255, 255, 0) #yellow
o = (255, 128, 0) #orange
n = (255, 128, 128) #pink
p = (128, 0, 128) #purple
d = (255, 0, 128) #darkPink
l = (128, 255, 128) #lightGreen

#Intro text or animation
# 3, 2, 1 countdown

class Game:
    def __init__(self):
        self.game_over = False
        self.catcher_x = 0
        self.berries = [
            {
                "name": "potato",
                "color": y,
                "pos_x": 0,
                "pos_y": 0,
                "points": 10
            },
            {
                "name": "blackberry",
                "color": w,
                "pos_x": 4,
                "pos_y": 0,
                "points": 2
            },
            {
                "name": "strawberry",
                "color": r,
                "pos_x": 6,
                "pos_y": 0,
                "points": 3
            },
            {
                "name": "blueberry",
                "color": b,
                "pos_x": 3,
                "pos_y": 0,
                "points": 4
            },
            {
                "name": "poison",
                "color": y,
                "pos_x": 2,
                "pos_y": 0,
                "points": -5
            }
        ]
        self.berry = choice(self.berries)
        self.berry_x = self.berry["pos_x"]
        self.berry_y = self.berry["pos_y"]
        self.berry_color = self.berry["color"]
        self.score = 0

    def move_left(self):
        if self.catcher_x >= 1:
            self.catcher_x -= 1
        else:
            self.catcher_x = 7

    def move_right(self):
        if self.catcher_x <= 6:
            self.catcher_x += 1
        else:
            self.catcher_x = 0


    def caughtit():
        if berry_x == catcher_x:
            score += berry["points"]
            sense.show_message(score)

    def berry_fall(self):
        if self.berry_y <= 7:
            self.berry_y += 1
            sleep(0.2)
            sense.set_pixel(self.berry_x, self.berry_y, self.berry_color)
        else:
            sense.show_message("GAME OVER")
            game_over = True
            sense.clear()
        
    def update(self):
        sense.clear()
        #berry_fall()
        if self.berry_y < 7:
            self.berry_y += 1
            sense.set_pixel(self.catcher_x, 7, d)
            sense.set_pixel(self.berry_x, self.berry_y, l)
            sleep(0.2)
        else:
            sense.show_message("GAME OVER")
            game_over = True
            sense.clear()
        sense.set_pixel(catcher_x, 7, d)

    def run(self):
        while game_over == False:
            self.update()
            for event in sense.stick.get_events():
                print(event)
                if event.action == "pressed" and event.direction == "left":
                    self.move_left()
                elif event.action == "pressed" and event.direction == "right":
                    self.move_right()
            sleep(0.1)
            self.update()

g = Game()
g.run()