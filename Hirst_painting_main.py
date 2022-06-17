# import colorgram
#
# colors = colorgram.extract('image.jpg', 36)
#
#
# print(f"initially the colors are in this format: {colors}" )
# colors_rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     colors_rgb.append(new_color)
#
#
# print(f"After formatting to a list of color tuples:  {colors_rgb}")
import turtle
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()


color_list = [(208, 155, 102), (55, 107, 129), (170, 80, 39), (124, 80, 97),
              (121, 155, 171), (197, 142, 37), (125, 175, 159), (224, 198, 133), (52, 37, 20), (189, 88, 109),
              (12, 46, 59), (189, 129, 145), (47, 166, 128), (60, 121, 113),
              (163, 21, 31), (216, 93, 78), (239, 167, 162), (39, 31, 33), (83, 145, 165), (8, 27, 26),
              (157, 28, 23), (233, 168, 172), (104, 126, 156), (22, 79, 88), (172, 205, 190), (167, 202, 209),
              (61, 60, 71), (34, 87, 85), (80, 63, 40), (177, 191, 209)]

turtle.colormode(255)

tim.speed(11)
tim.penup()
tim.ht()
tim.setx(-200)
tim.sety(-300)


def draw_a_spot_painting(size_of_square):
    for row in range(0, size_of_square):
        new_y = -300 + (row * 60)
        tim.goto(-300, new_y)

        for _ in range(0, size_of_square):
            tim.pendown()
            tim.color(random.choice(color_list))
            tim.begin_fill()
            tim.circle(15)
            tim.end_fill()
            tim.penup()
            tim.forward(60)


draw_a_spot_painting(10)


my_screen = Screen()
my_screen.exitonclick()
