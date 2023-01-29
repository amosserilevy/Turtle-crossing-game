import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()

screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() == 280:  # detect successful crossing
        player.go_to_start()
        car_manager.level_up()
        score.level_up()
        score.new_score()

    for car in car_manager.all_cars:  # detecting collision with car from the car list
        if player.distance(car) < 25:
            score.game_over()
            print("game over")
            game_is_on = False

    car_manager.create_car()
    car_manager.move_car()

screen.exitonclick()
