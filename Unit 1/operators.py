# Assignment Operators- Exclusively used to 
# assign values to variables
# key / value parings

# We use a single equal sign to respresent the assignment
# operator
name = "bryant"
grade = 10
school = True

# Arithmetic Operators - Used on numerical
# data types to perform calculations.
# intergers (whole numbers) and floats (decimal numbers)

# print is a function that lets us show code
# in the terminal
print(3 + 3) # addition operator
print(3 - 3) # subtraction operator
print(12 / 3) # division operator
print(3 * 4) # multiplication operator

# Comparison Operators - Set of symbols used
# to assess if data is the same or different and
# how they differ

print(10 > 1) # greater than operator
print(10 < 2) # less than operator

# 2 equal signs compare if something is the same
print ("kobe" == "Kobe") # same as (false)
print("2" == 2) # same as (false) not the same datatypes
print(2.0 == 2) # same as (true)

# not equal is written with !=
# this is to check and filter for values that are not 
# the same
print(200 != 100) # True- these are not the same
print(300 != 300) # False- these are the same



# logical operators- compares 2 conditions to check if 
# they are true or false

# And - checks if 2 conditions are true. if yes, the final
# result is true
print(3 > 1 and 100 > 50) # this would come out to be true

# OR- checks if only 1 condition is true. if yes,
# the final result will be true
print(3 > 1 or 100 > 50)

# Not - the "opposite day" operator. it will reverse the 
# result of the logical operators
print(not(3 > 1 and 100 > 50))
# this would come out to be fasle