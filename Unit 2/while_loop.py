# Loop - a loop is a construct (special function) that repeats itself.
# In programming, a loop allows to repeat code instructions.

# There are two types of loops: For loop and while loop

# While loop - a type of loop where so long as a condition is equal
# to true it will keep running forever.

# the keyword is while --> do while

# syntax
num = 4
while 2+2 == num: # condition --> operations
    print("the program is running...")

# while loops will ALWAYS run unless you change the condition!
# we can do this by writting instructions to manually change it.




def gussingGame():
    correctAnswer= 10
    userGuess= int(input("please type in a number to guess: "))
    attempts= 0

    while userGuess != correctAnswer:
        print("sorry thats incorrect ")
        print("try agian...")
        attempts +=1
        print("number of attempts: " + str(attempts))
        userGuess= int(input("please type in a number to guess: "))
       
    print("Congratulations! You guessed correctly! ")
    print("do you want to try again")

guessingGame()



while "userPassword" != "correctAnswer": 
     print("sorry thats incorrect ")
     print("try agian...")
     attempts -=1
     print("number of attempts: " + str(attempts))
     userPassword= int(input("please type in a number for password: "))
    