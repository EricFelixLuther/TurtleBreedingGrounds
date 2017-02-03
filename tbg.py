import turtle
import random
import time
import datetime
from __builtin__ import False


class TurtlesPolygon():
    def __init__(self, number_of_turtles=1, colorful=False, max_y=300, min_y=-300, max_x=300, min_x=-300):
        self.turtles = []
        self.top = max_y
        self.bot = min_y
        self.left = min_x
        self.right = max_x
        self._populate_turtles(number_of_turtles, colorful)
        self.constructor = MyTurtle()
        self.constructor.hideturtle()
        self._draw_boundaries()

    def _populate_turtles(self, number_of_turtles, colorful):
        for _ in xrange(number_of_turtles):
            if colorful:
                self.turtles.append(MyTurtle(color="random"))
            else:
                self.turtles.append(MyTurtle())

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

    def any_turtles_alive(self):
        return all(not each.is_alive for each in self.turtles)

    def go_turtles(self, kill_when_outside_boundaries=False):
        stop = False
        while not stop:
            for each in self.turtles:
                if each.is_alive:
                    each.forward(20)
                    each.left(each.get_random(0, 359))
                    if kill_when_outside_boundaries:
                        if not self.in_boundaries(*each.position()):
                            each.is_alive = False
            stop = self.any_turtles_alive()
        print("All turtles are dead.")

    def continuous_go_turtles(self):
        try:
            while True:
                self.constructor.restart()
                self._draw_boundaries()
                self.go_turtles(True)
                next_counter()
                for each in self.turtles:
                    each.restart()
        except KeyboardInterrupt:
            print("Bye")


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
        self.is_alive = True

    def get_random(self, x=0, y=100):
        return random.randint(x, y)

    def restart(self):
        self.clear()
        self.reset()
        self.hideturtle()

    def position(self, accurate=False):
        position = super(MyTurtle, self).position()
        if accurate:
            return position
        else:
            return (int(position[0]), int(position[1]))

    def compare_position(self, x=0, y=0, accurate=False):
        position = self.position(accurate)
        if accurate:
            return (x, y) == position
        else:
            return (int(x), int(y)) == position

    def pretty_shape(self, length=100, min_angle=1, max_angle=180, min_steps=2, max_steps=2):
        start_time = datetime.datetime.now()
        jumps = [self.get_random(min_angle, max_angle) for _ in xrange(self.get_random(min_steps, max_steps))]
        print jumps
        stop = False
        while not stop:
            for jump in jumps:
                self.forward(length)
                self.left(jump)
                if self.compare_position():
                    stop = True
        delta = datetime.datetime.now() - start_time
        print("Time taken to draw this picture: %s." % str(delta))

    def continuous_pretty_shape(self, length=100, min_angle=1, max_angle=180, min_steps=2, max_steps=2):
        while True:
            try:
                self.restart()
                self.pretty_shape(length, min_angle, max_angle, min_steps, max_steps)
                print("Done")
                next_counter()
            except KeyboardInterrupt:
                print("Bye")
                break


def next_counter():
    for i in xrange(0, 10):
        print("Next picture in: %d." % (10 - i))
        time.sleep(1)

stop = False
while not stop:
    print("Co chcesz?")
    print("1. Ladne ksztalty")
    print("2. Zolwie w ramce")
    x = raw_input()
    if x == '1':
        tp = MyTurtle()
        tp.continuous_pretty_shape(100, max_angle=90, min_steps=1, max_steps=5)
    elif x == '2':
        tp = TurtlesPolygon(10, True, 500, -500, 500, -500)
        tp.continuous_go_turtles()
    elif x == '':
        raw_input("Game over")
        stop = True
    else:
        print("Nie rozumiem.")
