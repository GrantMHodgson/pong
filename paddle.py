from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        # self.setheading(90)
        y_cor = self.ycor() + 20
        x_cor = self.xcor()
        self.goto(x_cor, y_cor)

    def move_down(self):
        y_cor = self.ycor() - 20
        x_cor = self.xcor()
        self.goto(x_cor, y_cor)
