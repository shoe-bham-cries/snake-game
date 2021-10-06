from turtle import Screen
import time
from food import Food
from snake import Snake
from socreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.right, key='d')

screen.update()
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect food
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    # Detect wall
    if (snake.snake_body[0].xcor() < -280) or (snake.snake_body[0].xcor() > 280) or (
            snake.snake_body[0].ycor() < -280) or (snake.snake_body[0].ycor() > 280):
        score.reset_score()
        snake.reset_snake()

    # Detect body
    for part in snake.snake_body[1:]:
        if snake.snake_body[0].distance(part) < 10:
            score.reset_score()
            snake.reset_snake()
screen.exitonclick()
