#main.py
from turtle import *
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width = 580, height = 580)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
turtles = []
position = [1, 2, 3]
screen.update()
game_on = True
tim = Turtle()
tim.penup()
tun = Turtle()
tun.penup()
snake = Snake()
sore = 00
food = Food(tim,tun,sore)

screen.listen()
screen.onkey(key="w", fun = snake.up)
screen.onkey(key="W", fun = snake.up)
screen.onkey(key="Up", fun = snake.up)
screen.onkey(key="a", fun = snake.left)
screen.onkey(key="A", fun = snake.left)
screen.onkey(key="Left", fun = snake.left)
screen.onkey(key="d", fun = snake.right)
screen.onkey(key="D", fun = snake.right)
screen.onkey(key="Right", fun = snake.right)
screen.onkey(key="s", fun = snake.down)
screen.onkey(key="S", fun = snake.down)
screen.onkey(key="Down", fun = snake.down)
screen.onkey(screen.bye, "Escape")
paused = False

def toggle_paused():
    global paused
    paused = not paused
    if paused:
        food.pause()
    else:
        food.resume()
        
screen.onkey(toggle_paused, "space")
while game_on:
    screen.update()
    time.sleep(0.1)
    if paused:
        continue 
    snake.auto_move()
    
    if snake.turtles[0].distance(food) < 17:
        food.refresh()
        sore += 1
        snake.make_longer()
        
    if food.scoreboard(tim, tun, sore):
        food.update_score(self,tun, sore)
        screen.update()
        
    if snake.detect_itself():
        game_on = False
    
    if not snake.border():
        game_on = False
       
    if game_on == False:
        food.game_over(sore)
        
    
screen.exitonclick()
