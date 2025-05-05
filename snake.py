#snake.py
from turtle import Turtle
import random
position = [1, 2, 3]
moving_dis = 20
colors = "lime"
up_ = 90
down_ = 270
right_ = 0
left_ = 180
class Snake:
    def __init__ (self):
        self.turtles = []
        self.create_snake()
        self.auto_direction = False
        
    def create_snake(self):
        for i in position:
            tim = Turtle(shape = "square")
            tim.penup()
            tim.color(colors)
            tim.goto(x = -20*i, y = 0)
            self.turtles.append(tim)
            self.create_eyes()
            
    def create_eyes(self):
        self.left_eye = Turtle()
        self.left_eye.penup()
        self.left_eye.shape("circle")
        self.left_eye.color("black")
        self.left_eye.shapesize(0.2)
        
        self.right_eye = Turtle()
        self.right_eye.penup()
        self.right_eye.shape("circle")
        self.right_eye.color("black")
        self.right_eye.shapesize(0.2)

            
    def auto_move(self):
        for i in range(len(self.turtles) -1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.turtles[0].fd(moving_dis)
        self.auto_direction = False
        
        head = self.turtles[0]
        heading = head.heading()
        if heading == 0:  
            offset_x, offset_y = 10, 5
        elif heading == 180:  # Left
            offset_x, offset_y = -10, 5
        elif heading == 90:   # Up
            offset_x, offset_y = 5, 10
        else:                 # Down
            offset_x, offset_y = 5, -10
        self.left_eye.goto(head.xcor() + 5, head.ycor() + 5)
        self.right_eye.goto(head.xcor() + 5, head.ycor() - 5)

    def up(self):
        if self.turtles[0].heading() != down_: 
            self.turtles[0].setheading(up_)
            self.direction_locked = True

    def down(self):
        if self.turtles[0].heading() != up_:
            self.turtles[0].setheading(down_)
            self.direction_locked = True

    def left(self):
        if self.turtles[0].heading() != right_:
            self.turtles[0].setheading(left_)
            self.direction_locked = True

    def right(self):
        if self.turtles[0].heading() != left_:
            self.turtles[0].setheading(right_)
            self.direction_locked = True

    def border(self):
        x = self.turtles[0].xcor()
        y = self.turtles[0].ycor()
        if x >= 300 or x <= -300 or y >= 300 or y <= -300:
            return False
        return True
    
    def make_longer(self):
        old_seg = self.turtles[-1]
        new_seg = Turtle(shape = "square")
        new_seg.color(colors)
        new_seg.penup()
        new_seg.goto(old_seg.xcor(), old_seg.ycor())
        self.turtles.append(new_seg)
    
    def detect_itself(self):
        for segments in self.turtles[1:]:
            if self.turtles[0].distance(segments) < 10:
                return True
        return False
    
    
        