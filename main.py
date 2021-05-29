import time
from turtle import Screen, Turtle
import paddle
import scorekeeper
import ball

# Set up screen for snake game
screen_width = 800
screen_height = 600
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


def draw_net():
    net = Turtle()
    net.penup()
    net.speed(10)
    net.goto(0, -300)
    net.setheading(90)
    net_pos = net.pos()[1]
    while net_pos < 300:
        net.dot(10, "white")
        net.forward(40)
        net_pos = net.pos()[1]


# initialize net, scoreboard, paddles
draw_net()
p1_score = scorekeeper.Scorekeeper((-60, 200))
p2_score = scorekeeper.Scorekeeper((60, 200))
p1_paddle = paddle.Paddle((-370, 0))
p2_paddle = paddle.Paddle((370, 0))
ball = ball.Ball()

screen.listen()
screen.onkey(p2_paddle.move_up, "Up")
screen.onkey(p2_paddle.move_down, "Down")

screen.onkey(p1_paddle.move_up, "w")
screen.onkey(p1_paddle.move_down, "s")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detect collision with top wall
    if ball.ycor() > 280:
        ball.change_y_direction(-1)
    # detect collision with bottom wall
    if ball.ycor() < -280:
        ball.change_y_direction(1)

    # detect collision with paddle 1
    if p1_paddle.distance(ball) < 50 and ball.xcor() < -320:
        ball.change_x_direction(1)
        ball.increase_speed()
    # detect collision with paddle 2
    if p2_paddle.distance(ball) < 50 and ball.xcor() > 320:
        ball.change_x_direction(-1)
        ball.increase_speed()

    # detect a point is scored for player 1
    if ball.xcor() > screen_width/2 - 20:
        p1_score.increase_score()
        ball.reset_ball(-1)
    # detect a point is scored for player 2
    if ball.xcor() < -1 * (screen_width/2) + 20:
        p2_score.increase_score()
        ball.reset_ball(1)


screen.exitonclick()
