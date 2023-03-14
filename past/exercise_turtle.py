import turtle

s = turtle.Screen()
s.bgcolor('cyan')

p = turtle.Pen()
p.shape('turtle')

# draw square


def draw_square(angle):
    for i in range(4):
        p.fd(100)
        p.left(angle)


p.goto(-100, 0)
# draw first square
p.fillcolor('red')
p.begin_fill()
draw_square(90)
p.end_fill()
# go forward 100 steps
p.fd(100)
# draw second square
p.fillcolor('green')
p.begin_fill()
draw_square(90)
p.end_fill()
# go backward 100 steps
p.bk(100)
# draw third square
p.fillcolor('orange')
p.begin_fill()
draw_square(-90)
p.end_fill()
# go forward 100 steps
p.fd(100)
# draw forth square
p.fillcolor('blue')
p.begin_fill()
draw_square(-90)
p.end_fill()
s.exitonclick()
