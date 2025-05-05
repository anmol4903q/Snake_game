#food&score_board.py
import random
from turtle import Turtle
tim = Turtle
class Food(Turtle):
    def __init__(self, tim,tun,sore):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.7, stretch_wid = 0.7)
        self.refresh()
        self.pause_writer = Turtle()
        self.pause_writer.hideturtle()
        self.pause_writer.color("red")
        self.pause_writer.penup()
        
    def refresh(self):
        xc = random.randint(-270, 270)
        yc = random.randint(-270, 260)
        xy = self.goto(xc, yc)
        
    def scoreboard(self, tim, tun, sore):
        tim.hideturtle()
        tim.color("white")
        tim.goto(0, 270)
        tim.write("Score = ",align = "center", font=("Courier", 12, "normal"))
        tun.hideturtle()
        tun.color("white")
        tun.goto(50, 270)
        tun.clear()
        tun.write(sore, align = "right", font=("Courier", 12, "normal"))
    
    def game_over(self, score):
        self.goto(0,0)
        self.write(f"GAME OVER!\nFinal Score: {score}", align="center", font=("Courier", 15, "bold"))
    
    def pause(self):
        self.pause_writer.clear()
        self.pause_writer.goto(0, 0)
        self.pause_writer.write("GAME PAUSED", align="center", font=("Courier", 15, "bold"))
        
    def resume(self):
        self.pause_writer.clear()
        