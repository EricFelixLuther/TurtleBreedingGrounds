import turtle
import random

class MyTurtles(turtle.Turtle):
    def __init__(self):
        super(MyTurtles, self).__init__()
        #self.setup(800, 600)
        self.showturtle()
	self.speed(0)
	self.tracer(1, 0)
	self.pretty_shape(length=100, min_angle=1, max_angle=90, min_steps=1, max_steps=5)

    def get_random(self, x=0, y=100):
        return random.randint(x, y)

    def genXY(self):
        self.x = self.get_random(1, 180)
        self.y = self.get_random(1, 180)

    def pretty_shape(self, length=100, min_angle=1, max_angle=180, min_steps=2, max_steps=2):
        self.clear()
        self.reset()
	jumps = [self.get_random(1, 90) for _ in xrange(self.get_random(min_steps, max_steps))]
	print jumps
	while True:
	    for jump in jumps:
		self.forward(length)
		self.left(jump)
	    pos = self.position()
	    pos_cosm = (int(pos[0]), int(pos[1]))
	    if pos_cosm == (0,0):
		break 
        

tp = MyTurtles()
raw_input("Done")
