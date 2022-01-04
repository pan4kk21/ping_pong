from turtle import Screen
from plates import Plate
from ball import Ball
from scoreboard import Score
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("PingPong")
my_screen.tracer(0)
my_screen.listen()

right_plate = Plate(350, 0)
left_plate = Plate(-350, 0)
ball = Ball()
score = Score()
game_is_on = True
time_sleep = 0.1

# Right plate
my_screen.onkey(right_plate.move_up, "Up",)
my_screen.onkey(right_plate.move_backwards, "Down")

# Left plate
my_screen.onkey(left_plate.move_up, "w")
my_screen.onkey(left_plate.move_backwards, "s")

while game_is_on:
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    time.sleep(time_sleep)
    my_screen.update()
    if ball.distance(right_plate) < 50 and ball.xcor() > 320 or ball.distance(left_plate) < 50 and ball.xcor() < -320:
        time_sleep -= 0.005
        ball.bounce_x()
    else:
        if ball.xcor() > 380:
            time_sleep = 0.1
            score.l_point()
            ball.home()
            ball.bounce_x()
        elif ball.xcor() < -380:
            time_sleep = 0.1
            score.r_point()
            ball.home()
            ball.bounce_x()

my_screen.exitonclick()
