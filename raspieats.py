from sense_hat import SenseHat 
import time
import random

sense = SenseHat()
sense.clear()

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

#image = [ 
 #   x, x, y, y, y, y, x, x, 
 #   x, y, y, y, y, y, y, x, 
  #  y, y, y, y, x, y, y, y, 
  #  y, y, y, y, y, y, xy, y, 
  #  y, y, y, x, x, x, x, x, 
  #  y, y, y, y, y, y, y, y, 
 #   x, y, y, y, y, y, y, x, 
   # x, x, y, y, y, y, x, x, 
#] 

#image = [ 
#    x, x, x, x, x, x, x, x, 
#    x, x, x, x, x, x, x, x, 
#    x, x, x, x, x, x, x, x, 
#    x, x, x, x, x, x, x, x, 
#    x, x, x, x, x, x, x, x, 
#    x, x, x, x, x, x, x, x, 
#    x, x, x, x, x, x, x, x, 
#    x, x, x, x, x, x, x, x, 
#] 

class Game:
    def __init__(self):
        self.player_x = 1
        self.player_y = 1
        self.food_x = 7
        self.food_y = 7
        self.is_hungry = True
        self.score = 0

        def reset(self):
            sense.clear
            self.player_x = random_randint(0, 7)
            self.player_y = random_randint(0, 7)
            same_spot = True
            while same_spot:
                self.food_x = random.randint(0,7)
                self.food_y = random.randint(0.7)
                if self.player_x != self.food_x and self.player_y != self.food_y:
                    same_spot = False
                    break

    def down(self):
        if self.player_y < 7:
            self.player_y += 1
            print("y:" + str(self.player_y))

    def up(self):
        if self.player_y <= 7:
            self.player_y -= 1
            print("y:" + str(self.player_y))
    
    def left(self):
        if self.player_x <= 7:
            self.player_x -= 1
            print("x" + str(self.player_x))

    def right(self):
        if self.player_x < 7:
            self.player_x += 1
            print("x:" + str(self.player_x))
    
    def update(self):
        sense.clear()
        sense.set_pixel(self.player_x, self.player_y, y)
        sense.set_pixel(self.food_x, self.food_y, l)

    def run(self):
        self.update()
        while self.is_hungry:
            for event in sense.stick.get_events():
                if event.direction == "down" and event.action == "released":
                    self.down()
                    self.update()
                if event.direction == "up" and event.action == "released":
                    self.up()
                    self.update()
                if event.direction == "left" and event.action == "released":
                    self.left()
                    self.update()
                if event.direction == "right" and event.action == "released":
                    self.right()
                    self.update()
                if self.player_x == self.food_x and self.food_y == self.player_y:
                    self.score += 1
                    sense.show_letter(str(self.score))
                    time.sleep(.5)
                    self.reset()
#                    sense.show_message("GAME OVER")
#                    self.is_hungry == False

                                    
                

#my_game = Game()
#my_game.run()
