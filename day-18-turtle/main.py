from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
screen.colormode(255)
tim.speed(0)

# for x in range(3, 10):
#     tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#     for i in range(x):
#         tim.forward(100)
#         tim.right(360/x)

direction = [0, 90, 180, 270]

for x in range(100):
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    tim.left(x)
    tim.circle(100)







screen.exitonclick()
