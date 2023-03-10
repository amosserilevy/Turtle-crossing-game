from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.new_score()

    def level_up(self):
        self.level += 1

    def new_score(self):
        self.clear()
        self.goto(x=-250, y=250)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
