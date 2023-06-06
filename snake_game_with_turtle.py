from turtle import Screen, Turtle
import time
from random import randint

snake_body = []


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


window = Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)

head = Turtle()
head.speed("fastest")
head.shape("square")
head.color("black")
head.penup()
head.direction = ""


food = Turtle()
food.speed("fastest")
food.shape("circle")
food.color("red")
food.penup()

change_food_position()

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")


while True:
    window.update()

    if head.distance(food) < 20:
        change_food_position()
        # TODO ایجاد بدن جدید و اضافه کردن به لیست

    move()
    time.sleep(0.1)
