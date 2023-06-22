
from turtle import Turtle
from random import randint


def make_turtle(turtle_shape, turtle_color):
    my_turtle = Turtle()
    my_turtle.speed("fastest")
    my_turtle.shape(turtle_shape)
    my_turtle.color(turtle_color)
    my_turtle.penup()
    return my_turtle


def change_food_position(food):
    food_x = randint(-240, 240)
    food_y = randint(-240, 240)
    food.goto(food_x, food_y)
