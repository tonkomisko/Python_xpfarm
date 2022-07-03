from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", False, "center", ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", False, "center", ("Courier", 80, "normal"))

    def increase_lscore(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_rscore(self):
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self, side):
        self.goto(0, 0)
        self.write(f"GAME OVER {side} WINS!", align=ALIGNMENT, font=FONT)


