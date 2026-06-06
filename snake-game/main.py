import turtle
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

s = turtle.Screen()
s.bgcolor("black")
s.screensize(400,400)
s.tracer(0) # Turn off automatic screen updates
s.title("Snake Game")


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

is_game_on = True

# Game Over function




while is_game_on:
      s.update() 
      time.sleep(0.1) 
      snake.move()


      # Detect collision with food
      if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
      
      # Detect collision with wall
      if abs(snake.head.xcor()) > 295 or abs(snake.head.ycor()) > 295:
            scoreboard.reset_score()
            snake.reset_snake()

      # Detect collision with tail
      for segment in snake.segments[1:]:
            if snake.head.position() == segment.position():
                  scoreboard.reset_score()
                  snake.reset_snake()





      s.listen()
      s.onkey(snake.up, "Up")
      s.onkey(snake.down, "Down")
      s.onkey(snake.left, "Left")
      s.onkey(snake.right, "Right")







s.exitonclick()