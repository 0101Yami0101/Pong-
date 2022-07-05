from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self,x,y):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1
        
    def move(self):
        newX = int(self.xcor() + self.x_move)
        newY = int(self.ycor() + self.y_move)
        self.goto(newX,newY)

    def bounce_y(self):
        self.y_move *= -1  #reverse direction

    def bounce_x(self):
        self.x_move *= -1  #reverse direction
        self.ball_speed *= 0.8 #speed of ball increases when bounce off

    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()


      
