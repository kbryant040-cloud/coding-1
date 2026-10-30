# What is a loop --> Code thats repeats.

# While loops = a block code that repeats itself until the triggering
# conditions is no longer TRUE. CAN BE INFINITE

# For loops = a type of loop (code block that repeats itself) BUT
# it only repeats itself upto a certain number of times. IT IS FINITE

# THINIK OF FOR LOOPS AS THE COUNTING LOOP

# FOR LOOP SYNTAX
# i stand for itertator = programers decided make this the universal
# symbol for a placeholder for counting

for i in range(1,10):
    print(i)


# LIST --> a data collection type that acts as a container for
# multiple data types--> a way to list multiple pieces of data
# in 1 place

foodItem_1 = "apple"

grocerlist = ["apples","oranges","water","chips","ground beef"]

print(groceryList)

for i in grocerList:
    print("I need to buy " + i)

grades = [100, 98, 75, 77, 89, 80]

for grade in grades:
    # show me the grades lower than 85
    if grade < 85:
        print(grade)


# lists are collection types for us to store multiple peices of
# data in one location

# one benefit of using lists is that they can be manipulated
# (change/mutable)

# we use list methods to modify our lists

inventory = ["weapons", "healing potion", "sheild", "armor"]

# When we want to add an item to a list we use the append() method
inventory.append("spell book")
print(inventory)

# List are index based- meaning we can search and find values inside of 
# list because it structed

# To pull a specific value from a list, use the list index position
# lists always start from 0.
print(inventory[0])

# Find the method for removing an item from a list- specifically,
# remove the healing potion

inventory.remove("healing position")
inventory.pop(1)

print(inventory)

# How do we add the healing potion back to our inventory
# list-specifically at index 3
inventory.insert(3, "healing potion")