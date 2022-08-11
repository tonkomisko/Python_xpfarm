import turtle
# import math
# import time
from math import *

# sun = turtle.Turtle()
# sun.shape('circle')
# sun.color('yellow')


class Planet(turtle.Turtle):

    def __init__(self, name, radius, color):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.penup()
        self.up()
        self.pd()
        self.angle = 0

    def move(self):
        x = self.radius*cos(self.angle)
        print(f"{self.name}'x coordinate is {x} now")
        # mercury on first iteration of the move - x= 39.9
        # y = 40 * sin(0 + 0.05) = 40 * 8.726 = 436
        y = self.radius*sin(self.angle)
        print(f"{self.name}'y coordinate is {y} now")
        # print(f"y is {y} now")
        # self.penup()
        self.goto(0 + x, 0 + y)
        # self.pendown()







