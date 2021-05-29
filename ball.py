from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(10)
        self.color("white")
        self.y_direction = 1
        self.x_direction = 1
        self.movement_pixels = 5

    def change_y_direction(self, direction):
        self.y_direction = direction

    def change_x_direction(self, direction):
        self.x_direction = direction

    def move(self):
        xcor = self.xcor() + (self.movement_pixels * self.x_direction)
        ycor = self.ycor() + (self.movement_pixels * self.y_direction)
        self.goto(xcor, ycor)

    def reset_ball(self, direction):
        self.goto(0, 0)
        self.x_direction = direction
        self.movement_pixels = 5

    def increase_speed(self):
        self.movement_pixels += 10
