from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # print(f"the y move is: {self.y_move}")
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # print(f"new bounce y move is: {self.y_move}")

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.home()
        self.move_speed = 0.1
        # to move the ball to the opposite position
        self.bounce_x()
