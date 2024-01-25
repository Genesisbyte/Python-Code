#Title: Shapes in Python: Diamond
#Date: 11-Jan-2024
#Author Genesisbyte
#Description: Creating a diamond
 
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

#Drawing the diamond        
t.setheading(135) #Rotating the square
Shape(75,4,0,0) #Drawing the diamond with size 75 with sides of 4

#Text on the screen
t.color ("Red")
t.write("Finished!",font=("Ariel",40,"italic"))
