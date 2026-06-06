import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")





game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.increase_score()




    screen.update()
    time.sleep(0.08)






screen.exitonclick()