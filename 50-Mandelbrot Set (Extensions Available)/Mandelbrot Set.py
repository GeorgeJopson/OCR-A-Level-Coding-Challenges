import turtle
from math import ceil,floor,sqrt
import cmath
##Commented out code made to test functionality previously
##def makeColor(distanceFromCenter):
##    distanceFromCenter+=1
##    color=int(floor(255/distanceFromCenter))
##    return (color,color,color)
def mandelbrot(complexNum):
    maxIterations=80
    counter=0
    z=0
    while abs(z) <=2 and counter<=80:
        z=z**2+complexNum
        counter+=1
    if(counter>=maxIterations):
        return True
    else:
        return False
screen=turtle.getscreen()
screen.colormode(255)
turtle.bgcolor("white")
turtle.shape("circle")
turtleSize=80
turtle.turtlesize(turtleSize/20,turtleSize/20)
turtle.penup()
turtle.goto(turtleSize/2 - screen.window_width()/2, screen.window_height()/2 - turtleSize/2)
resolution=int(input("Input the resolution you want: "))
for line in range(9):
    for pixel in range(9):
##        distanceFromCenter=sqrt((4-line)**2+(4-pixel)**2)
##        turtle.color(makeColor(distanceFromCenter))
        if(mandelbrot(complex((pixel-4)/resolution,(line-4)/resolution))):
            turtle.color("black")
        else:
            turtle.color("grey")
        turtle.stamp()
        if(pixel!=0 and pixel!=8):
            turtle.fd(turtleSize)
        elif(pixel==0):
            if(line==0):
                turtle.fd(turtleSize)
            elif(line%2==1):
                turtle.rt(90)
                turtle.fd(turtleSize)
            else:
                turtle.lt(90)
                turtle.fd(turtleSize)
        elif(pixel==8):
            if(line%2==0):
                turtle.rt(90)
                turtle.fd(turtleSize)
            else:
                turtle.lt(90)
                turtle.fd(turtleSize)
turtle.ht()
