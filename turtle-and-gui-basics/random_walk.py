import turtle as t
import random


tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)
t.bgcolor("black")

def random_color():
      r = random.randint(0, 255)
      g = random.randint(0, 255)
      b = random.randint(0, 255)
      return (r, g, b)

# Drawing a spirograph with radius 100 and 360 circles
# def draw_spirograph():
#       for _ in range(360):
#             tim.color(random_color())
#             tim.circle(100) # Draw a circle with radius 100
#             tim.right(10) # Rotate the turtle by 10 degree to create a spirograph effect


# Drawing a spirograph with radius 100 and 360/size_of_gap circles | size_of_gap is the angle between each circle | the code stops when the turtle has completed a full circle (360 degree)
def draw_spirograph(size_of_gap):
      for _ in range(360 // size_of_gap):
            tim.color(random_color())
            tim.circle(100) # Draw a circle with radius 100
            tim.right(size_of_gap) # Rotate the turtle by size_of_gap degree to create a spirograph effect


draw_spirograph(5)

t.done()