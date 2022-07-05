#PONG

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG BY YAMI")
screen.tracer(0)
#main Objects
paddle1 = Paddle((350,0))
paddle2 = Paddle((-350,0))
newBall = Ball(280,380)
scoreboard = Scoreboard()

#Listen
screen.listen()
#paddle! controls
screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle1.go_down, "Down")
#paddle2 controls
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle2.go_down, "s")


game_on = True
while game_on:
    screen.update()
    time.sleep(newBall.ball_speed)
    newBall.move()
    #detect collision with wall
    if newBall.ycor() > 280 or newBall.ycor() < -280 or newBall.xcor() > 380 or newBall.ycor() <-280:
        #bounceepass
        newBall.bounce_y()

    #Detect collision with paddles
    if newBall.distance(paddle1) < 50 and newBall.xcor() > 330 or newBall.distance(paddle2) < 50 and newBall.xcor() < -330:
        newBall.bounce_x()

    #detect when paddle1 misses
    if newBall.xcor() > 380:
        newBall.reset_position()
        scoreboard.left_point()
       

    #detect when paddle2 misses
    if newBall.xcor() < -380:
        newBall.reset_position()
        scoreboard.right_point()
        
        



screen.exitonclick()