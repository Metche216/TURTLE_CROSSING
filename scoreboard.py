from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-250,y=250)
        self.lvl = 1
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f'Level:{self.lvl}',False, align='left',font=FONT,)
        
    def lvl_passed(self):
        self.lvl += 1
        self.update_score()