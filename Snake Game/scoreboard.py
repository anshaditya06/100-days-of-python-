from turtle import Turtle


class ScoreBoard(Turtle):
      def __init__(self):
            super().__init__()
            self.score = 0
            with open("Snake Game/highscore.txt", "r") as file:
                  self.highscore = int(file.read())
            self.color("white")
            self.hideturtle()
            self.penup()
            self.goto(0, 270)
            self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))
            
      def update_score(self):
            self.clear()
            self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 24, "normal"))
      
      def increase_score(self):
            self.score += 1
            self.update_score()
      
      def reset_score(self):
            if self.score > self.highscore:
                  self.highscore = self.score

            with open("Snake Game/highscore.txt", "w") as file:
                        file.write(str(self.highscore))      
            self.score = 0
            self.update_score()