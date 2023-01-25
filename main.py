import random
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40),
              (218, 87, 49), (174, 178, 231), (237, 169, 164), (6, 245, 223), (247, 9, 42), (10, 79, 112),
              (16, 54, 243), (240, 16, 16)]

my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.goto(-250, -200)
my_turtle.pendown()
my_turtle.pensize(30)


def draw_line():

    for _ in range(10):
        my_turtle.speed(1)
        my_turtle.color(random.choice(color_list))
        my_turtle.forward(1)
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()


for _ in range(10):
    draw_line()
    my_turtle.penup()
    my_turtle.speed(0)
    my_turtle.goto(my_turtle.pos() + (-510, 50))
    my_turtle.pendown()
    my_turtle.speed(1)

my_screen = Screen()
my_screen.exitonclick()
