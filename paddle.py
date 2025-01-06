from turtle import Turtle
WINDOW_WIDTH=700
WINDOW_HEIGHT=700

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle=[]

    def create_paddle(self,pos_x,):
        pos_y=0
        positions=[(pos_x,pos_y),(pos_x,pos_y+20),(pos_x,pos_y+40)]
        for point in positions:
            part=Turtle()
            part.penup()
            part.speed(10)
            part.goto(point)
            part.shape("square")
            part.color("white")
            self.paddle.append(part)

    def up(self):
        if self.paddle[2].ycor()>((WINDOW_HEIGHT/2)-70):
            return
        self.paddle[2].setheading(90)
        for part in range(0,len(self.paddle)-1):
            pos_x=self.paddle[part+1].xcor()
            pos_y=self.paddle[part+1].ycor()
            self.paddle[part].goto(pos_x,pos_y)
        self.paddle[2].forward(20)

    def down(self):
        if self.paddle[0].ycor()<(((-1)*WINDOW_HEIGHT/2)+40):
            return
        self.paddle[0].setheading(270)
        for part in range(len(self.paddle)-1,0,-1):
            pos_x=self.paddle[part-1].xcor()
            pos_y=self.paddle[part-1].ycor()
            self.paddle[part].goto(pos_x,pos_y)
        self.paddle[0].forward(20)