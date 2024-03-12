from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("magenta")
        self.speed("fastest")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(random_x, random_y)

