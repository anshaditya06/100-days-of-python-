# import os
# import colorgram


# current_dir = os.path.dirname(__file__)
# image_path = os.path.join(current_dir, "image.jpg")

# # Extracting the colors from the image using colorgram library
# colors = colorgram.extract(image_path, 30)


# rgb_colors = []
# for color in colors:
#       r = color.rgb.r
#       g = color.rgb.g
#       b = color.rgb.b
#       rgb_colors.append((r, g, b))

# print(rgb_colors)

import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

turtle.colormode(255)

# Example color list (you can replace with extracted colors)
color_list = [(245, 243, 239), (247, 242, 244), (204, 164, 107), (239, 245, 241), (155, 73, 46), (235, 238, 244), (52, 92, 123), (224, 201, 135), (171, 153, 40), (138, 31, 21), (132, 162, 185), (200, 91, 71), (48, 122, 87), (14, 99, 73), (95, 73, 75), (146, 178, 147), (72, 47, 38), (163, 142, 158), (234, 175, 165), (55, 46, 50), (184, 206, 172), (19, 85, 90), (144, 21, 24), (41, 62, 74), (82, 145, 128), (181, 87, 89), (41, 66, 90), (13, 71, 68), (213, 178, 183), (179, 191, 207)]

# Starting position (bottom-left)
# t.setheading(225)
# t.forward(300)
# t.setheading(0)

t.setposition(-250, -250)  # Move to the bottom-left corner

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    # Move to next row after every 10 dots
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

turtle.done()
