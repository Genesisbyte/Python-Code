#Title: Shapes in Python: Triangle
#Date: 11-Jan-2024
#Author Genesisbyte
#Description: Triangle Drawing


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

#Drawing the triangle
t.setheading(180)
Shape(500,3,100,100)#size of 500 by 3 sides with position of 100,100





