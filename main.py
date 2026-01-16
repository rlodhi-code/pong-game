from turtle import Screen, Turtle
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # turns off the animation

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    screen.update()

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    screen.update()


screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.listen()
screen.update()

screen.exitonclick()
