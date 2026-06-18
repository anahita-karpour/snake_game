from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "italic")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.hideturtle()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
