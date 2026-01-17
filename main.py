import sys
from sys import displayhook
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # turns off the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball=Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce
        ball.bounce_y()

    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    #detect if ball as gone passed the side walls
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()

