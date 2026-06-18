import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Create the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Turn off auto-rendering so the screen only updates when we tell it to.
# This prevents flickering during movement.
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(new_snake.turn_up, "Up")
screen.onkey(new_snake.turn_down, "Down")
screen.onkey(new_snake.turn_left, "Left")
screen.onkey(new_snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # Controls game speed
    new_snake.move()

    # Detect collision with food
    if new_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        new_snake.extend()

    # Detect collision with the wall
    if (
        new_snake.head.xcor() > 280
        or new_snake.head.xcor() < -280
        or new_snake.head.ycor() > 280
        or new_snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the snake's own tail
    for segment in new_snake.segments_lst[1:]:  # bypass the head segment
        if new_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
