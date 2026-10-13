# When we are building complex programs, we need a
# way to pass in data that is NOT always
# from the user

# Funtion Parameters- this is PLACEHOLDER DATA for
# a function. variable insdie the curly brackets

# Funtion arguments and parameters are ways to
# pass in data to a funtion from possibly
# another function.

# memory trick - PAMERTER AND PLACEHOLDER BOTH
# START WITH THE LETTER P
def check_Water_Depth(depth):
    print(depth)
    print(depth > 10) # true if depth is greater than 10 feet
    # return depth

# Function Arguments- This is the REAL DATA that we pass into
# the function call.
# memory trick- if you make a REAL world arguments with a person
# you need to come with REAL facts (data)
check_Water_Depth(3)

# return - this keyboard allows us to pass data from INSIDE 1 function
# into another function

def username(name):
    return name 

def confirmLogin(username):
    name = username(username)
    print(name)