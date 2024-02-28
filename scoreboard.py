from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 250)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 16, "normal"))
