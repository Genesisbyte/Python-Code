#Title: Add Numbers
#Date: 11-Feb-2024
#Author: Genesisbyte
#Description: Adding two numbers

#Libraries
from tkinter import *
import tkinter.messagebox as box                        #Assigning variable box as messagebox


#Instances
win=Tk()                                                #Assigning variable win to Tk()

#Procedure to name and resize the window
def WindowSize(title):  
    win.title(title)                                    #Creating the title to be edited
    win.geometry("400x400")                             #Window size of 300x300 (height x width)

#Procedure to quit the program
def QuitProgram():
    quit()                                              #quit() means to quit the program

#Procedure to display label
def DisplayLabel(labelTitle):
    label=Label(win,text=labelTitle,font=("Arial",25))
    label.pack()

#Procedure to create and display the quit button
def ExitButton():
    qButton=Button(win,text="Exit",font=("Arial",10),command=QuitProgram) #Create the quit button named Quit with the command of QuitProgram procedure
    qButton.place(x=150,y=180)                          #Display the button and placed at co-ordinates 130x130 with .place()

#Procedure to empty the fields
def ClearEntry():
    e1.delete(0,END)                                    #Delete the entry field after output. .delete(0,END) means delete from first character at 0 all the way to the end of the string
    e2.delete(0,END)                                    #Delete the entry field after output. .delete(0,END) means delete from first character at 0 all the way to the end of the string

#Procedure to create and display an errormessage
def DisplayError(x):
    box.showerror("Error")

#Procedure to create and display the outcome
def DisplayMessage(x):
    box.showinfo("Answer",x)                            #Display the output of the calculation with the messagebox title named info

#Procedure to add the inputs
def AddResult(x,y):
    if x==int(x)and y==int(y):                              #If 1st and second inputs are integers
        DisplayMessage(int(x)+int(y))                       #Then display message with answer being an int
    elif x==float(x) and y==float(y):                       #If 1st and 2nd inputs are floats
        DisplayMessage(float(x)+float(y))                   #Then call DisplayMessage with answer being a float
    elif x==float(x) and y==int(y):                         #If 1st input is a float and second input an int
        DisplayMessage(float(x)+int(y))                     #Then call DisplayMessage with answer being adding a float and int
    elif x==int(x) and y==float(y):                         #If 1st input an int and 2nd input a float
        DisplayMessage(int(x)+float(y))                     #Then call DisplayMessage with answer being adding a int and float
    #If not concerned with answer being float regardless
    #Just use DisplayMessage(x+y)                           

#Procedure to add the two inputs and display the answer
def AddSum():
    try:
        number1=float(e1.get())                             #Convert user input for first entry box into an float and store as number 1
        number2=float(e2.get())                             #Convert user input for second entry box into an floatand store as number 2
    except ValueError:
        DisplayError("Error! Enter numbers only!")          #Call DisplayError procedure if above code produces ValueError
    else:                                                       
        AddResult(number1,number2)                          #Otherwise call AddResult procedure 
    

l1=Label(win,text="Enter first number",font=("Arial",15))   #Prompt for for first number
l1.place(x=50,y=60)                                         #Display label and place automatically with .pack()
e1=Entry(win)                                               #Create input box
e1.place(x=250,y=65)                                        #Display input box

l2=Label(win,text="Enter second number",font=("Arial",15))  #Prompt for second number
l2.place(x=50,y=90)                                         #Display label and place automatically with .pack()
e2=Entry(win)                                               #Create input box
e2.place(x=250,y=95)                                        #Display input box


addButton=Button(win,text="Add!",font=("Arial",10),command=lambda:([AddSum(),ClearEntry()]))  #Create the Add! button and using lambda pass functions to submit info and to clear the entry fields afterwards to start again
addButton.place(x=150,y=150)                                                #Place button at co-ordinates 300 by 200

#Calling procedures
WindowSize("Adding two numbers")                        #Calling WindowSize with the title of adding two numbers
DisplayLabel("Adding two numbers")
ExitButton()                                            #Calling the QuitButton procedure to display the quit button

#Mainloop means to run the tk loop
win.mainloop()
