import turtle
import random
import time
import datetime

class TurtlesPolygon():
    def __init__(self, number_of_turtles=1, colorful=False, max_y=300, min_y=-300, min_x=-300, max_x=300):
        self.turtles = []
        self.top = max_y
        self.bot = min_y
        self.left = min_x
        self.right = max_x
        for _ in xrange(number_of_turtles):
            if colorful:
                self.turtles.append(MyTurtle(color="random"))
            else:
                self.turtles.append(MyTurtle())
        self.constructor = MyTurtle()
        self.constructor.hideturtle()
        self._draw_boundaries()

    def _draw_boundaries(self):
        self.constructor.penup()
        self.constructor.goto(self.left, self.top)
        self.constructor.pendown()
        for length in [abs(self.left) + abs(self.right),
                       abs(self.top) + abs(self.bot),
                       abs(self.left) + abs(self.right),
                       abs(self.top) + abs(self.bot)]:
            self.constructor.forward(length)
            self.constructor.right(90)
        self.constructor.penup()
        self.constructor.goto(0, 0)
        self.constructor.pendown()

    def in_boundaries(self, x, y):
        if y < self.top and \
                y > self.bot and \
                x < self.right and\
                x > self.left:
            return True
        else:
            return False

    def go_turtles(self, kill_when_outside_boundaries=False):
        while self.turtles != []:
            for each in self.turtles:
                each.forward(20)
                each.left(each.get_random(0, 359))
                if kill_when_outside_boundaries:
                    if not self.in_boundaries(*each.position()):
                        del self.turtles[self.turtles.index(each)]
        print("All turtles are dead.")


class MyTurtle(turtle.Turtle):
    def __init__(self, color=None):
        super(MyTurtle, self).__init__()
        #self.setup(800, 600)
        self.showturtle()
        self.speed(0)
        self.tracer(1, 0)
        self.screen.colormode(255)
        if color:
            if color == "random":
                self.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            elif type(color) == str or type(color) != str and len(color) == 1:
                self.pencolor(color)
            else:
                self.pencolor(*color)

    def get_random(self, x=0, y=100):
        return random.randint(x, y)

    def restart(self):
        self.clear()
        self.reset()
        self.hideturtle()

    def position(self, accurate=False):
        position = super(MyTurtle, self).position()
        if accurate:
            return (int(position[0]), int(position[1]))
        else:
            return position

    def compare_position(self, x=0, y=0, accurate=False):
        position = self.position(accurate)
        if accurate:
            return (int(x), int(y)) == position
        else:
            return (x, y) == position
            

    def pretty_shape(self, length=100, min_angle=1, max_angle=180, min_steps=2, max_steps=2):
        start_time = datetime.datetime.now()
        jumps = [self.get_random(1, 90) for _ in xrange(self.get_random(min_steps, max_steps))]
        print jumps
        while True:
            for jump in jumps:
                self.forward(length)
                self.left(jump)
                if self.compare_position():
                    break
        delta = datetime.datetime.now() - start_time
        print("Time taken to draw this picture: %s." % str(delta))

    def continuous_pretty_shape(self, length=100, min_angle=1, max_angle=180, min_steps=2, max_steps=2):
        while True:
            try:
                self.restart()
                self.pretty_shape(length, min_angle, max_angle, min_steps, max_steps)
                print("Done")
                for i in xrange(0, 10):
                    print("Next picture in: %d." % (10 - i))
                    time.sleep(1)
            except KeyboardInterrupt:
                print("Bye")
                break


def draw_pretty_shapes():
    tp = MyTurtle()
    tp.continuous_pretty_shape(100, max_angle=90, min_steps=1, max_steps=5)

def do_random_stuff():
    tp = TurtlesPolygon(10, True)
    try:
        tp.go_turtles(kill_when_outside_boundaries=True)
    except KeyboardInterrupt:
        print("Bye")
    raw_input("Game over")

do_random_stuff()
#draw_pretty_shapes()