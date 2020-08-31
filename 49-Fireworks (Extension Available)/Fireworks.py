import turtle
from random import randint
from math import floor
def fly(turtle,steps,stepSize,turn):
    for step in range(steps):
        turtle.left(randint(-turn,turn))
        turtle.forward(stepSize)

colors=[]

screen=turtle.getscreen()
screen.colormode(255)
turtle.bgcolor("black")
while True:
    rocket=turtle.Turtle()
    rocket.ht()
    rocket.speed(0)
    rocket.penup()
    rocket.goto(randint(-screen.screensize()[0]*0.8,screen.screensize()[0]*0.8),-screen.screensize()[0])
    rocket.pendown()
    rocket.pencolor((randint(1,255),randint(1,255),randint(1,255)))
    rocket.left(90)
    fly(rocket,randint(5,15),randint(25,75),randint(5,15))
    sparkles=[]
    sparkleColor=(randint(1,255),randint(1,255),randint(1,255))
    numOfSparkles=randint(6,12)
    for sparkle in range(numOfSparkles):
        sparkles.append(turtle.Turtle())
        sparkles[sparkle].ht()
        sparkles[sparkle].speed(0)
        sparkles[sparkle].penup()
        sparkles[sparkle].goto(rocket.position())
        sparkles[sparkle].pendown()
        sparkles[sparkle].color(sparkleColor)
        sparkles[sparkle].left((360/numOfSparkles)*sparkle)
        fly(sparkles[sparkle],randint(7,12),randint(7,12),randint(10,15))
