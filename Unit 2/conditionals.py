# Conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions

# condititional syntax (how it is written)
bill_amount = int(input("please type in a bill tender (1,5,10) "))

# if usually indicates that something is a possible option
if bill_amount == 1:
    print("here are 4 quarters")
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
elif bill_amount == 5:
    print("here are 20 quareters")
elif bill_amount == 10
     print("here are 50 quarters")
elif bill_amount == 20
     print("sorry cant accepts")

# else is ALWAYS your last option
else:
     print("sorry amount entered is not correct. your burnt")


def colloge():
    grade= int(input("please type in your grade: "))
    if grade > 90:
        templeUApp()
    else:
        ccApp()


# Using the calaulator functions from the calculator.py file,
# Create a main calculator function that uses if/else logic to
# allow the user to selct different arithmetic operators and
# then perfrom those operations by running their respective functions.

# Example: an input where if the user enter q, it will run the addition function.
# 1= addition()
# 2= subtraction()
# 3= multiplication()
# 4= division()

def calculate_add():
    print("program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print(num1 + num2)
    print("program has ended. ")


choice = input("please a number: ")

if choice == '1':
    calculate_add()
elif choice == '2':



# Class Assignment

def movieTicket():
    print("Welcome to the movie theater. Please type in your age ")
    age = int(input())
    if age <= 7:
        print("your ticket is 8.00. ")
    elif age >= 8 and age <= 20:
        print('your ticket is 12.00') 
    elif age >= 21 and age <= 60:
        print('your ticket is 20.00')
    elif age >=61:
        print("your ticket is free. ")
    else:
        print("sorry there was an error in the program...")

movieTicket()