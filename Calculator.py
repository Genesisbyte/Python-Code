#Title: Creating a Calculator GUI
#Date: 11-Feb-2024
#Author: Dean Clipsham
#Description: Calculator

#Libraries
from tkinter import *
import tkinter.messagebox as box                        #Assigning the string box as messagebox


#Instances
win=Tk()                                                #Assigning "win" as Tk

#Procedure to name and resize the window
def WindowSize(title):  
    win.title(title)                                    #Creating the title to be edited
    win.geometry("500x400")                             #Window size of 500x400 (height x width)

#Procedure to display label
def DisplayLabel(lbl):
    label=Label(win,text=lbl,font=("Arial",25))         
    label.place(x=175,y=30)

#Procedure to display error
def DisplayError(x):
    box.showerror("Error",x)                        

#Procedure to create and display the outcome
def DisplayMessage(x):
    box.showinfo("Info",x)                              #Display the output of the calculation

#Procedure to quit the program
def QuitProgram():
    quit()                                              #Quit the program


#Procedure to create and display the quit button
def ExitButton():
    qButton=Button(win,text="Exit",command=QuitProgram) #Create the quit button when pressed program will quit
    qButton.place(x=225,y=350)                          #Display the button and placed at 225 by 350

#Procedure to add inputs and print answer
def AddResult(x,y):
    if x==int(x)and y==int(y):                          #If 1st and second inputs are integers
        DisplayMessage(int(x)+int(y))                   #Then display message with answer being an int
    elif x==float(x) and y==float(y):                   #If 1st and 2nd inputs are floats
        DisplayMessage(float(x)+float(y))               #Then call DisplayMessage with answer being a float
    elif x==float(x) and y==int(y):                     #If 1st input is a float and second input an int
        DisplayMessage(float(x)+int(y))                 #Then call DisplayMessage with answer being adding a float and int
    elif x==int(x) and y==float(y):                     #If 1st input an int and 2nd input a float
        DisplayMessage(int(x)+float(y))                 #Then call DisplayMessage with answer being adding a int and float
    #If not concerned with answer being float
    #just use DisplayMessage(x+y)
    

#Procedure to subtract inputs and print answer
def MinusResult(x,y):
    if x==int(x)and y==int(y):
        DisplayMessage(int(x)+int(y))
    elif x==float(x) and y==float(y):
        DisplayMessage(float(x)-float(y))
    elif x==float(x) and y==int(y):
        DisplayMessage(float(x)-int(y))
    elif x==int(x) and y==float(y):
        DisplayMessage(int(x)-float(y))                 
    #If not concerned with answer being float
    #just use DisplayMessage(x-y)
    
#Procedure to multiply inputs and print answer
def MultiplyResult(x,y):
    if x==int(x)and y==int(y):
        DisplayMessage(int(x)*int(y))
    elif x==float(x) and y==float(y):
        DisplayMessage(float(x)*float(y))
    elif x==float(x) and y==int(y):
        DisplayMessage(float(x)*int(y))
    elif x==int(x) and y==float(y):
        DisplayMessage(int(x)*float(y))                                #Call DisplayMessage procedure to display the total of 1st input x 2nd input
    #If not taking too seriously
    #just use DisplayMessage(x*y)
    
#Procedure to divide inputs and print answer
def DivideResult(x,y):
    if x==int(x)and y==int(y):
        DisplayMessage(int(x)/int(y))
    elif x==float(x) and y==float(y):
        DisplayMessage(float(x)/float(y))
    elif x==float(x) and y==int(y):
        DisplayMessage(float(x)/int(y))
    elif x==int(x) and y==float(y):
        DisplayMessage(int(x)/float(y))                                 #Call DisplayMessage procedure to display the total of 1st input / 2nd input
    #If not concerned with answer being float
    #just use DisplayMessage(x/y)

#Procedure to calculate the power of two inputs
def PowerResult(x,y):
    if x==int(x)and y==int(y):
        DisplayMessage(int(x)**int(y))
    elif x==float(x) and y==float(y):
        DisplayMessage(float(x)**float(y))
    elif x==float(x) and y==int(y):
        DisplayMessage(float(x)**int(y))
    elif x==int(x) and y==float(y):
        DisplayMessage(int(x)**float(y))                            #x to the power of y using ** as operator
    #If not concerned with answer being float
    #just use DisplayMessage(x**y)


#Procedure to clear the entry fields after output displayed
def Clear():
    num1entry.delete(0,END)              #Delete the entry field after output. .delete(0,END) means delete from first character at 0 all the way to END
    num2entry.delete(0,END)              #Delete the entry field after output. .delete(0,END) means delete from first character at 0 all the way to END

#Procedure for adding numbers
def AddSum():
    try:                                                        #Attempt to perform below action
        number1=float(num1entry.get())                          #Convert user input for first entry box into an float and store as number1
        number2=float(num2entry.get())                          #Convert user input for second entry box into an float and store as number2
    except ValueError:                                          #If number1 or number2 produce a ValueError....
        DisplayError("Enter numbers only")                      #Call DisplayError procedure
    else:
        AddResult(number1,number2)                              #Otherwise add result
    
                                      
#Procedure for subtracting numbers
def MinusSum():
    try:                                                        #Attempt to perform below action
        number1=float(num1entry.get())                          #Convert user input for first entry box into an float and store as number1
        number2=float(num2entry.get())                          #Convert user input for second entry box into an float and store as number2
    except ValueError:
        DisplayError("Enter numbers only")                
    else:                                       
        MinusResult(number1,number2)                            #Call MinusResult procedure with parameters of the two inputs      
                                  
#Procedure for dividing numbers
def DivideSum():
    try:
        number1=float(num1entry.get())                          #Convert user input for first entry box into an float and store as number1
        number2=float(num2entry.get())                          #Convert user input for second entry box into an float and store as number2
    except ValueError:
        DisplayError("Enter numbers only")                        #Call DisplayError procedure
    else:
        DivideResult(number1,number2)                           #Call DivideResult procedure with parameters of the two inputs      
                                 
    
#Procedure for multiplying numbers
def MultiplySum():
    try:
        number1=float(num1entry.get())                          #Convert user input for first entry box into an float and store as number1
        number2=float(num2entry.get())                          #Convert user input for second entry box into an float and store as number2
    except ValueError:
        DisplayError("Enter numbers only")                      #Call DisplayError procedure
    else:
        MultiplyResult(number1,number2)                         #Call MultiplyResult procedure with parameters of the two inputs

#Procedure for finding the power
def PowerSum():
    try:
        number1=float(num1entry.get())                          #Convert user input for first entry box into an float and store as number1
        number2=float(num2entry.get())                          #Convert user input for second entry box into an float and store as number2
    except ValueError:
        DisplayError("Enter numbers only")                      #Call DisplayError procedure
    else:
        PowerResult(number1,number2)                            #Call PowerResult procedure with parameters of the two inputs


#Creating the labels and entries                                 
num1label=Label(win,text="Enter number",font=("Arial",15))
num1label.place(x=50,y=100)
num1entry=Entry(win)
num1entry.place(x=200,y=110)

num2label=Label(win,text="Enter number",font=("Arial",15))
num2label.place(x=50,y=200)
num2entry=Entry(win)
num2entry.place(x=200,y=200)

#Code to create buttons with commands
addButton=Button(win,text="+",command=lambda:([AddSum(),Clear()]))      #Create the addition button and using lambda pass functions to display output and to clear the entry fields afterwards to start again
addButton.place(x=180,y=250)                                            #Placed at co-ordinates 180 x 250

minButton=Button(win,text="-",command=lambda:([MinusSum(),Clear()]))    #Create the subtraction button and using lambda pass functions to display output and to clear the entry fields afterwards to start again
minButton.place(x=210,y=250)                                            #Placed at co-ordinates 210 x 250

divButton=Button(win,text="/",command=lambda:([DivideSum(),Clear()]))   #Create the division button and using lambda pass functions to display output and to clear the entry fields afterwards to start again
divButton.place(x=240,y=250)                                            #Placed at co-ordinates 240 x 250

multButton=Button(win,text="x",command=lambda:([MultiplySum(),Clear()]))#Create the multiplication button and using lambda pass functions to display output and to clear the entry fields afterwards to start again
multButton.place(x=270,y=250)                                           #Placed at co-ordinates 270 x 250

powerButton=Button(win,text="xʸ",command=lambda:([PowerSum(),Clear()])) #Create the multiplication button and using lambda pass functions to display output and to clear the entry fields afterwards to start again
powerButton.place(x=300,y=250)                                          #Placed at co-ordinates 300 x 250


    
#Calling procedures
DisplayLabel("Calculator")
WindowSize("Calculator")                                
ExitButton()                                           

#Run the tk widgets and gui until user enters quit button
win.mainloop()

#Note
#Personally believe there are too many procedures for something as "simple" as this
