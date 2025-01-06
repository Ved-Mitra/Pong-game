from turtle import Turtle
from random import randint
WINDOW_WIDTH=700
WINDOW_HEIGHT=700

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(3)
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # make turtle shape 20*0.5=10px
        self.color("blue")
        self.setheading(randint(1,355))

    def bounce(self): #according to law of reflection
        direction=self.heading()
        if self.ycor() > ((WINDOW_WIDTH/2)-40) or self.ycor() < ((-1)*(WINDOW_WIDTH/2)+20):
            self.setheading(360-direction)
        else:
            self.setheading(180-direction)

    def move(self):
        self.forward(15)