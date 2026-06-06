import turtle

t = turtle.Turtle()
s = turtle.Screen()

def move_forward():
      t.forward(10)

def move_backward():
      t.backward(10)

def turn_left():
      t.left(10)

def turn_right():
      t.right(10)

def clear_screen():
      t.clear()
      t.penup()
      t.home()
      t.pendown()

s.listen()
s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(turn_left, "a")
s.onkey(turn_right, "d")
s.onkey(clear_screen, "c")

s.exitonclick()