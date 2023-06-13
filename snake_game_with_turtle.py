from turtle import Screen, Turtle
import time
from random import randint

snake_body = []
score = 0
high_score = 0


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def change_food_position():
    food_x = randint(-240, 240)
    food_y = randint(-240, 240)
    food.goto(food_x, food_y)


def make_turtle(turtle_shape, turtle_color):
    my_turtle = Turtle()
    my_turtle.speed("fastest")
    my_turtle.shape(turtle_shape)
    my_turtle.color(turtle_color)
    my_turtle.penup()
    return my_turtle


def reset():
    head.goto(0, 0)
    head.direction = ""
    for body in snake_body:
        body.hideturtle()

    snake_body.clear()


window = Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)
window.tracer(0)


head = make_turtle("square", "black")
head.direction = ""


food = make_turtle("circle", "red")

change_food_position()

score_pen = make_turtle("square", "white")
score_pen.goto(0, 260)
score_pen.hideturtle()
score_pen.write(
    f"Score : {score}, High Score: {high_score}", align="center", font=38)


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")


while True:
    window.update()

    if head.distance(food) < 20:
        change_food_position()
        # TODO اضافه کردن امتیاز
        # score_pen.clear()

        new_body = make_turtle("square", "grey")
        snake_body.append(new_body)

    for i in range(len(snake_body) - 1, 0, -1):
        x_prev = snake_body[i-1].xcor()
        y_prev = snake_body[i-1].ycor()
        snake_body[i].goto(x_prev, y_prev)
    if len(snake_body) > 0:
        x_head = head.xcor()
        y_head = head.ycor()
        snake_body[0].goto(x_head, y_head)

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset()

    move()


    # TODO در صورت برخورد به بدن ببازد
    time.sleep(0.2)
