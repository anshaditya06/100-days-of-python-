import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 2 # velocity of ball in x direction
        self.dy = 2 # velocity of ball in y direction
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9 # increase speed after each paddle hit



    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01 # reset move speed
        self.dx *= -1