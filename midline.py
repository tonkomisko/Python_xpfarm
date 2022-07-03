from turtle import Turtle


class Midline(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.setheading(270)
        self.color("white")
        self.penup()
        self.goto(0, 280)
        while self.ycor() > -290:
            self.pendown()
            self.fd(15)
            self.penup()
            self.fd(15)
