# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# for x in range(20):
#     color = colors[x]
#     rgb = color.rgb
#     rgbcolor = (rgb.r, rgb.g, rgb.b)
#     color_list.append(rgbcolor)
# print(color_list)
from turtle import Turtle
from turtle import Screen
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77)]
tim.shape("circle")

tim.penup()
tim.setheading(200)
tim.forward(300)
tim.speed("fastest")

def starting_position():
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(90)
    tim.forward(50)

for i in range(10):
    for x in range(10):
        tim.color(random.choice(color_list))
        tim.stamp()
        tim.setheading(0)
        tim.forward(50)
    starting_position()
tim.hideturtle()




screen.exitonclick()

