import turtle
# import math
from math import cos, sin


class Planet(turtle.Turtle):
    def __init__(self, name, radius, color):
        super().__init__()
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.shape("circle")
        self.up()
        self.pd()
        self.angle = 0

    def move(self):
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)

        self.goto(0 + x, 0 + y)
