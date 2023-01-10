import turtle
import time

s = turtle.Screen()
s.title("My app")
s.bgcolor('orange')
s.bgpic('mario.png')
# s.register_shape('my_shape', ((0, 0), (1, 1)))
# s.register_shape('my_shape', ((1, 1), (0, 0), (-1,1)))
# s.register_shape('strawberry.gif')

p = turtle.Pen()
# 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
# p.shape('my_shape')
# p.shape('strawberry.gif')
p.shape('turtle')
p.shapesize(3, 3, 3)

# p.penup()
# p.goto(100, 100)
# p.pendown()
p.pensize(4)
p.pencolor('red')
# for i in range(4):

#     p.forward(100)
#     p.left(90)

# for i in range(3):
#     p.forward(100)
#     p.left(120)

# for i in range(5):
#     p.fd(100)
#     p.lt(72)

# for i in range(6):
#     p.fd(100)
#     p.left(60)
###################################
# for i in range(4):

#     p.forward(100)
#     p.rt(90)

# for i in range(3):
#     p.forward(100)
#     p.rt(120)

# for i in range(5):
#     p.fd(100)
#     p.rt(72)

# for i in range(6):
#     p.fd(100)
#     p.rt(60)


# کشیدن ستاره
p.penup()
p.setpos(-90, 30)

p.pendown()
for i in range(5):
    p.forward(200)
    p.right(144)
    # time.sleep(10)


p.penup()
p.setpos(80, -140)

p.write("سلام", font=85)
p.hideturtle()


s.exitonclick()
