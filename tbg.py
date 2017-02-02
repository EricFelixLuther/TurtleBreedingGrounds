import turtle
import random

class MyTurtles(turtle.Turtle):
    def __init__(self):
        super(MyTurtles, self).__init__()
        #self.setup(800, 600)
        self.showturtle()
	self.pretty_shape()

    def genXY(self):
        self.x = random.randint(1,180)
        self.y = random.randint(1,180)
        
    def pretty_shape(self):
        self.clear()
        self.reset()
	self.genXY()
        print str(self.x) + " " + str(self.y)
        stop = False
        while stop == False:
            self.forward(100)
            self.left(self.x)
            self.forward(100)
            self.left(self.y)
            pos = self.position()
            pos_cosm = (int(pos[0]), int(pos[1]))
            if pos_cosm == (0, 0):
                stop = True

tp = MyTurtles()
