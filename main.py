from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen= Screen()
screen.setup(width=600,height=600)
screen.bgcolor("red")
screen.title("Snake game - Maaz ")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# turnoff-the-screen

# starting_position=[(0,0),(-20,0),(-40,0)]
# segments = []
# this is concept of tuples

# for position in starting_position:
#     new_segment=Turtle("square")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)


# segment_1 = Turtle("square")
# segment_2 = Turtle("square")     or u can chnge the position by for loop
# segment_2.goto(-20,0)
# segment_3 = Turtle("square")
# segment_3.goto(-40,0)
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep((0.1))

    snake.move()

    # distance method detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #     detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #     detect collision ith tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # it will update the screen

    # for seg in segments:
    #
    #     seg.forward(20)
    #     time.sleep((0.1))


    # aisa loop banao ki left turn krne pr 2nd snake 1st k jagah le aur 3rd snake 2nd ka

    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    #     # segments[0].forward(20)
    #     # # segments[0].left(90)
    # segments[0].forward(20)
    # segments[0].left(90)


screen.exitonclick()