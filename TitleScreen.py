#Title: Menu
#Date: 18-Jan-2024
#Author: Genesisbyte
#Description: Title Screen with 5 options

import sys #Import system library

def Menu(): #Print "title screen"
    print('Speedster')
    print('==============================')
    print('1. Start Game')
    print('2. New Game')
    print('3. Load Game')
    print('4. Options')
    print('5. Quit')
    
#Call menu procedure    
Menu()

def Choice():
    while True: #Loop until correct option has been entered
        userChoice=input("What option do you want? ")
        if userChoice =="1":
            print("You have chosen Start Game")
            sys.exit() #Close program when this option has been entered
        elif userChoice=="2":
            print("You have chosen New Game")
            print("Select difficulty: Casual,Normal,Hard") #Prompt user for difficulty options 
        if userChoice.upper()=="CASUAL":
            print ("Starting game on Casual")
            sys.exit()
        elif userChoice.upper()=="NORMAL":
            print ("Starting game on Normal")
            sys.exit()
        elif userChoice.upper()=="HARD":
            print ("Starting game on Hard")
            sys.exit()
        elif userChoice=="3":
            print ("You have chosen Load Game")
            sys.exit()
        elif userChoice=="4":
             print("You have chosen Options")
             
        elif userChoice=="5":
            print ("Quitting game")
            break#Exit loop if Quit Game option has been entered
        else:
            print("Only enter from options in menu")#Error catch 
         
      
        
#Call choice procedure           
Choice()







