import turtle
from random import randint
screen=turtle.getscreen()
screen.colormode(255)
turtle.bgcolor("black")
pen=turtle.Turtle()
pen.color("yellow")
pen.ht()
while True:
    pen.penup()
    x=randint(-screen.screensize()[0],screen.screensize()[0])
    y=randint(-screen.screensize()[1],screen.screensize()[1])
    pen.goto(x,y)
    pen.pendown()
    for point in range(6):
        pen.fd(10)
        pen.bk(10)
        pen.right(60)
