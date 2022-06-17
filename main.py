#####Turtle Intro######
import turtle
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
t.colormode(255)


# random_color = random.choice()
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)


######## Challenge 1 - Draw a Square ############


# todo 1: draw a square by dividing the 360 by 4 and finding the angle degrees
# in the turtle doc find function that uses angles as parameter

# turtle_color = random.choice(tim.color)
# print(tim.color)

# def random_color():
#     random_red = random.randrange(0, 256, 20)
#     random_green = random.randrange(0, 256, 20)
#     random_blue = random.randrange(0, 256, 20)
#
#     # turtle.color(random_red, random_green, random_blue)
#     return random_red, random_green, random_blue


# random_colors = ["green", "blue", "red", "coral", "black", "violet",
#                  "hot pink", "indigo", "firebrick"]

# #
# for side in range(3, 20):
#     tim.color(random.choice(random_colors))
#
#     for _ in range(0, side):
#         angle = 360 / side
#         tim.forward(100)
#         tim.right(angle)
#

# challenge 4 random walk using random directions

# random_directions = [0, 90, 180, 270]
#
#
def random_color():
    random_r = random.randint(0, 255)
    random_g = random.randint(0, 255)
    random_b = random.randint(0, 255)
    rand_color = (random_r, random_g, random_b)
    return rand_color


#
#
# def random_walk():
#     tim.seth(random.choice(random_directions))
#     tim.color(random_color())
#     tim.width(10)
#     tim.forward(30)
#     tim.speed(10)
#     turtle.ontimer(random_walk, 1000)
#
#
# random_walk()
#
# heading = 0

tim.speed("fastest")


def draw_a_spirograph(tilt_degree):
    for _ in range(int(360 / tilt_degree)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + tilt_degree)


draw_a_spirograph(5)

my_screen = Screen()
my_screen.screensize(500, 1500)
# # my_screen.textinput("testing", "click to close me")
my_screen.exitonclick()
