import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_l = 0
        self.score_r = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Player A: {self.score_l}  Player B: {self.score_r}", align="center", font=("Courier", 24, "normal"))

    def increase_score_l(self):
        self.score_l += 1
        self.update_score()

    def increase_score_r(self):
        self.score_r += 1
        self.update_score()