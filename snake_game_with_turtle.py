import turtle
import time

def go_up():
    if head.direction != "down":
        head.direction = "up"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    # TODO اضافه کردن جهت چپ و راست


window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("blue")
window.setup(width=600, height=600)

head = turtle.Turtle()
head.shape("square")
head.penup()
head.direction = "none"

window.listen()
window.onkey(go_up, "Up")

# TODO اضافه کردن سایر جهت ها


while True:
    window.update()
    move()
    time.sleep(0.1)
