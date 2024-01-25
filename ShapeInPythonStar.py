#Title: Shapes in Python Star
#Date: 11-Jan-2024
#Author Dean Clipsham
#Description: Star drawing program

#Libraries
import turtle
 
#Initialise
t=turtle.Turtle()

for loop in range(3): #Loop 3 times
        t.forward(100)  # Move the turtle forward by 100 pixels
        t.right(120)    # Turn the turtle right by 120 degrees

t.penup() #Pick pen up
t.goto(0,-50) #Place turtle at these coordinates

t.pendown()#Place pen down


for loop in range(3): #Loop 3 times
    t.forward(100) #Move turtle forward 100 pixels
    t.left(120)    #Turn turle  left by 120 degrees


