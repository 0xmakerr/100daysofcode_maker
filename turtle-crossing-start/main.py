import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


screen.listen()
scoreboard = Scoreboard()
player = Player()
screen.onkey(player.move, "Up")
car_manager = CarManager()

cars = []
for _ in range(220):
    cars.append(CarManager())

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    move_speed = scoreboard.score * 2
    for car in cars:
        car.move(move_speed + 5)
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.finish_line()
        scoreboard.new_score()

screen.exitonclick()
