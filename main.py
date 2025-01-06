from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=700,height=700)
screen.title("paddle game")
screen.tracer(0)

def game_setup():
    """To set up the game window"""
    setup=Turtle()
    setup.color("white")
    setup.goto(x=0,y=(-1)*screen.window_height()/2)
    setup.goto(x=0,y=screen.window_height()/2)
    setup.penup()
    setup.goto((-1)*screen.window_width()/2,screen.window_height()/2-30)
    setup.pendown()
    setup.goto(screen.window_width()/2,screen.window_height()/2-30)

#asking for game mode
mode=0
while mode !=1 and mode !=2:
    mode=int(screen.numinput("Game-Mode","Select your Game-Mode\n1. Player Vs. Computer\n2. Player Vs. Player\nEnter 1 or 2"))
player1 = Paddle()  # creates player's paddle
player1.create_paddle((-1)*(screen.window_width()/2)+20)
player2 = Paddle()  # creates computer's paddle
player2.create_paddle(screen.window_width()/2-30)
if mode==1:
    screen.listen()
    screen.onkeypress(player1.up, "Up")
    screen.onkeypress(player1.down, "Down")
elif mode==2:
    screen.listen()
    screen.onkeypress(player1.up, "w")
    screen.onkeypress(player1.down, "s")
    screen.onkeypress(player2.up, "Up")
    screen.onkeypress(player2.down, "Down")

#creating the ball
ball=Ball()

#creating scoreboard
score1=ScoreBoard()
score1.position(-90,screen.window_width()/2-30)
score2=ScoreBoard()
score2.position(90,screen.window_width()/2-30)

game_is_on=True
game_setup()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # checking for collision with wall
    if ball.ycor() > (screen.window_height()/2-40) or ball.ycor() < ((-1)*screen.window_height()/2+20):
        ball.bounce()

    # detect collision with paddle of player-1
    for part in player1.paddle:
        if part.distance(ball) < 30:
            score1.point()
            ball.bounce()
            # to avoid repetative errors in score
            ball.move()
            ball.move()
            break

    if mode==1:
        # detect collision with paddle of player-2
        for part in player2.paddle:
            if part.distance(ball) < 30:
                score2.point()
                ball.bounce()
                # to avoid repetative errors in score
                ball.move()
                ball.move()
                break

        #controlling the computer paddle
        if ball.ycor()<player2.paddle[1].ycor():
            player2.down()
        elif ball.ycor()>player2.paddle[1].ycor():
            player2.up()

        # checking if paddle missed the ball
        if ball.xcor()>(screen.window_width()/2-10):
            game_is_on=False
            if score1.score>score2.score:
                score1.you_won()
            else:
                score1.you_lose()
        if ball.xcor()<((-1)*screen.window_width()/2+10):
            game_is_on=False
            if score1.score > score2.score:
                score1.you_won()
            else:
                score1.you_lose()

    if mode==2:
        #detect collision with paddle of player2
        for part in player2.paddle:
            if part.distance(ball) < 30:
                score2.point()
                ball.bounce()
                # to avoid repetative errors in score
                ball.move()
                ball.move()
                break

        # checking if paddle missed the ball
        if ball.xcor() > (screen.window_width() / 2 - 10):
            game_is_on = False
            if score1.score > score2.score:
                score1.p1_won()
            else:
                score1.p2_won()
        if ball.xcor() < ((-1) * screen.window_width() / 2 + 10):
            game_is_on = False
            if score1.score > score2.score:
                score1.p1_won()
            else:
                score1.p2_won()

screen.exitonclick()