from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
game_is_on = True


def pause():
    global game_is_on
    game_is_on = False


def game_over():
    global game_is_on
    game_is_on = True


tim = Turtle()
tim.pencolor("white")
tim.penup()
tim.setposition(0, -300)
tim.setheading(90)
for _ in range(40):
    tim.pendown()
    tim.fd(10)
    tim.penup()
    tim.fd(10)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(game_over, "q")

r_score = Score(200, 240)
l_score = Score(-200, 240)
while game_is_on:
    screen.update()
    ball.starting_move()
    time.sleep(ball.ball_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        l_score.add_score()
        ball.reset()

    if ball.xcor() < -380:
        r_score.add_score()
        ball.reset()







screen.exitonclick()
