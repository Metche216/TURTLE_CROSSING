from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LIST = []
CARS_QTY = 50


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.resizemode('user')
        self.shapesize(1,2)
        self.penup()
        self.goto(x=340,y=random.randint(-220,220))
        self.moving_speed = MOVE_INCREMENT*-1
        CAR_LIST.append(self)
        
        
        
    def move(self):
        self.goto(x=self.xcor() + self.moving_speed,y=self.ycor())
        
    
