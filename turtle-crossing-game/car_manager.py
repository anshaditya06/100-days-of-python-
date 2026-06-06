COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import turtle
import random

class CarManager(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = turtle.Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-230, 230))
            new_car.move_speed = self.move_speed
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(car.move_speed)

    def increase_speed(self):
        for car in self.cars:
            car.move_speed += MOVE_INCREMENT
   