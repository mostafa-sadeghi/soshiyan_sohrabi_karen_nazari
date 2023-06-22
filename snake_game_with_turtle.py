from turtle import Screen
import time

from snake_game_utils import make_turtle, change_food_position


snake_body = []
score = 0
try:
    f = open("snake_game.txt","r")
    high_score = int(f.read())
    # print(high_score)
    # print(type(high_score))
except:
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







def reset():
    global score
    f = open("snake_game.txt", "w")
    f.write(str(score))
    score = 0
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

change_food_position(food)

score_pen = make_turtle("square", "white")
score_pen.goto(0, 260)
score_pen.hideturtle()


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")


while True:
    window.update()
    score_pen.clear()
    score_pen.write(
        f"Score : {score}, High Score: {high_score}", align="center",
        font=("Arial", 22))
    if head.distance(food) < 20:
        change_food_position(food)
        score += 1
        if score > high_score:
            high_score = score

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

    for body in snake_body:
        if body.distance(head) < 20:
            reset()

    time.sleep(0.2)


# exception Handling    مدیریت کردن استثنائات

# try:
#     n1 = int(input('> '))
#     n2 = int(input('> '))
#     print(n1/n2)
# except:
#     print(0)
