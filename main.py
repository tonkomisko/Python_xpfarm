from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from midline import Midline
import time

RIGHT_POSITION = (350, 0)
LEFT_POSITION = (-350, 0)
GAME_GOAL = 3

my_screen = Screen()
my_screen.setup(800, 600)
my_screen.bgcolor("black")
my_screen.title("PONG")
my_screen.tracer(0)

right_paddle = Paddle(RIGHT_POSITION)
left_paddle = Paddle(LEFT_POSITION)

game_ball = Ball()
scoreboard = Scoreboard()
midline = Midline()

# game_ball.move_ball()

my_screen.listen()
my_screen.onkey(right_paddle.go_up, "Up")
my_screen.onkey(right_paddle.go_down, "Down")

my_screen.onkey(left_paddle.go_up, "w")
my_screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    # while midline.position() > (0, -280):
    #     midline.draw_line()
    time.sleep(game_ball.move_speed)
    my_screen.update()
    game_ball.move_ball()

    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        # while game_ball.xcor() < 350:
        game_ball.bounce_y()

    if game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320 or \
            game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320:
        game_ball.bounce_x()

    if game_ball.xcor() > 390:
        game_ball.reset_ball()
        scoreboard.increase_lscore()
        if scoreboard.l_score == GAME_GOAL:
            scoreboard.game_over("left")
            game_is_on = False

    if game_ball.xcor() < -390:
        game_ball.reset_ball()
        scoreboard.increase_rscore()
        if scoreboard.r_score == GAME_GOAL:
            scoreboard.game_over("right")
            game_is_on = False

my_screen.exitonclick()
