from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# move the last block to the position of the second to last block,
# second to last to the position of the block before it


class Snake:
    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        for block in STARTING_POSITION:
            snake_block = Turtle(shape="square")
            snake_block.color("white")
            snake_block.penup()
            snake_block.goto(block)
            self.snake_blocks.append(snake_block)

    def move(self):
        for seg_num in range(len(self.snake_blocks)-1, 0, -1):
            new_x = self.snake_blocks[seg_num - 1].xcor()
            new_y = self.snake_blocks[seg_num - 1].ycor()
            self.snake_blocks[seg_num].goto(new_x, new_y)
        self.snake_blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
