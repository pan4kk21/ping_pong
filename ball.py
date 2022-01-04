from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x=x + self.x_move, y=y + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
