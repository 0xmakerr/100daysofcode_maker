from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 50


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.random_x = random.randint(-280, 5000)
        self.random_y = random.randint(-230, 280)
        self.goto(self.random_x, self.random_y)

    def move(self, move_speed):
        new_x = self.xcor() - move_speed
        self.goto(new_x, self.random_y)
