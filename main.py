# Title: Employee Creation
# Date: 29-Feb-2024
# Author: Genesisbyte
# Description: Employee Information


# Class
class Employee:
    __name = ""         # Creating name variable with __ meaning its private
    __dob = ""          # Creating dob variable with __ meaning its private
    __age = ""          # Creating age variable with __ meaning its private
    __salary = 0        # Creating salary variable with __ meaning its private

    # Create function to set details
    def set_details(self):
        try:
            self.__name = input("Enter name: ")             # Ask for name with variable from above class
            self.__dob = input("Enter DOB: ")               # Ask for DOB  with variable from above class
            self.__age = int(input("Enter age: "))          # Ask for age  with variable from above class
            self.__salary = int(input("Enter salary: "))    # Ask for salary with variable from above class
        except ValueError:      # If wrong input entered for above statements
            print("Invalid Input")  # Print message
        else:
            user_input = input("Press any key to continue or x to quit")    # Ask user for choice
            if user_input.lower() == "x":       # If user enters x regardless of upper or lower
                return                  # Exit the loop

        self.set_details()              # Recursively loop the function

    # Function to display the information
    def show_details(self):
        print(f"Name:{self.__name}")    # Print name
        print(f"DOB:{self.__dob}")      # Print DOB
        print(f"Age:{self.__age}")      # Print age
        print(f"Salary:{self.__salary}")    # Print salary


# Create main function
def main():
    emp1 = Employee()  # Create first object named emp1
    emp2 = Employee()  # Create second object named emp2
    emp3 = Employee()  # Create third object named emp3
    emp1.set_details()  # Set details of first loop to emp1
    emp1.show_details()  # Show details on x being entered
    emp2.set_details()  # Set details of second loop to emp2
    emp2.show_details()  # Show details on x being entered
    emp3.set_details()  # Set details of third loop to emp3
    emp3.show_details()  # Show details on x being entered


# Calling the "main" function
main()
