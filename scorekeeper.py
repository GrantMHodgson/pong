from turtle import Turtle


class Scorekeeper(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed(10)
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.update()

    def update(self):
        self.clear()
        print("updating score")
        self.write(str(self.score), align='center', font=('Courier', 80, 'normal'))

    def increase_score(self):
        self.score = self.score + 1
        self.update()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align='center', font=('Times New Roman', 21, 'normal'))
