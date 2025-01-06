from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()

    def point(self):
        self.score+=1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"{self.score}",align="center",font=('Arial',15,'normal'))

    def position(self,pos_x,pos_y):
        self.goto(pos_x,pos_y)
        self.display_score()

    def you_lose(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER",align="center",font=('Arial',15,'bold'))
        self.goto(x=0,y=-30)
        self.write(f"YOU LOSE", align="center", font=('Arial', 15, 'bold'))

    def you_won(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=('Arial', 15, 'bold'))
        self.goto(x=0, y=-30)
        self.color("green")
        self.write(f"You Won", align="center", font=('Arial', 15, 'bold'))

    def p1_won(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=('Arial', 15, 'bold'))
        self.goto(x=0, y=-30)
        self.color("green")
        self.write(f"Player-1 Won", align="center", font=('Arial', 15, 'bold'))

    def p2_won(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=('Arial', 15, 'bold'))
        self.goto(x=0, y=-30)
        self.color("green")
        self.write(f"Player-2 Won", align="center", font=('Arial', 15, 'bold'))