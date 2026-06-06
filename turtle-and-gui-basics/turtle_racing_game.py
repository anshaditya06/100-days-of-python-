import turtle
import random

s = turtle.Screen()
width = s.window_width()
height = s.window_height()

user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]

turtles = []

for turtle_index in range(6):
    t = turtle.Turtle()
    t.shape("turtle")
    t.shapesize(stretch_wid=2, stretch_len=2)
    t.penup()
    t.goto(- width/2 + 50, y_positions[turtle_index])
    t.color(colors[turtle_index])
    turtles.append(t)



if user_bet:
    is_race_on = True
    

while is_race_on:
    for racer in turtles:
        if racer.xcor() > width/2 - 50:
            is_race_on = False
            winning_color = racer.pencolor()

    # Clear all racer turtles
            for t in turtles:
                  t.hideturtle()

    # Create result writer
            result_turtle = t
            result_turtle.hideturtle()
            result_turtle.penup()
            result_turtle.goto(0, 0)

            if winning_color == user_bet.lower():
                  message = f"You've won! The {winning_color} turtle wins!"
            else:
                  message = f"You've lost! The {winning_color} turtle wins!"

            result_turtle.write(
                  message,
                  align="center",
                  font=("Arial", 20, "bold")
            )
    
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




s.exitonclick()