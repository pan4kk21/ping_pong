from turtle import Turtle


class Plate(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def move_backwards(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)
