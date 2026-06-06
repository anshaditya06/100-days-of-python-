import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

s = turtle.Screen()
s.bgcolor("black")
s.screensize(600,600)
s.title("Pong Game")
s.tracer(0)

r_paddle = Paddle((300, 0))
l_paddle = Paddle((-300, 0))
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkeypress(r_paddle.move_up, "Up")
s.onkeypress(r_paddle.move_down, "Down")
s.onkeypress(l_paddle.move_up, "w")
s.onkeypress(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()
    #Detect collision with top and bottom walls
    if abs(ball.ycor())>330:
        ball.bounce_y()
    #Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 280) or (ball.distance(l_paddle) < 50 and ball.xcor() < -280):
        ball.bounce_x()

    #Detect right paddle misses
    if ball.xcor() > 330:
        ball.reset_position()
        scoreboard.increase_score_l()

    #Detect left paddle misses
    if ball.xcor() < -330:
        ball.reset_position()
        scoreboard.increase_score_r()
    

s.exitonclick()