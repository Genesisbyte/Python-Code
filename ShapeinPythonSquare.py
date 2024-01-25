#Title: Shapes in Python (Square)
#Date: 11-Jan-2024
#Author Genesisbyte
#Description: Creating a square
 

#Libraries
import turtle
 
#Initialise
t=turtle.Turtle()


#Create a procedure
def Shape(length,sides,x,y):
    t.shape("turtle")
    t.speed(10)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for loop in range(sides):
        t.forward(length)
        angle=360/sides
        t.rt(angle)

#Calling the Square procedure
Shape(100,4,0,0)


