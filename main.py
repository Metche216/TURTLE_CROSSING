import time
from turtle import Screen
from player import Player
from car_manager import CarManager, CAR_LIST as CL, CARS_QTY as CQ
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_1 = Player()



screen.listen()

screen.onkeypress(player_1.move, 'Up')


game_is_on = True
while game_is_on:
    car_fire = random.randint(1,3)
    time.sleep(0.1)
    screen.update()
    
    if len(CL) < CQ:
        if car_fire == 1:
            car = CarManager()
            
            
    
    if player_1.ycor() >260:
        player_1.reset()
    
    
    
    #CHECK IF CARRER ENDED
    for car in CL:
        if car.xcor() < -340:
            CL.remove(car)
            del car
        else:
            car.move()
    
    