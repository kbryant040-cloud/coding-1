def vending_machine():
    while True:
        number = input("Enter a vending machine number (or q to quit): ").upper()

        if number == "B3":
            print("You got Nacho Chips!")
        elif number == "G4":
            print("You got BBQ Chips!")
        elif number == "G7":
            print("You got Plain Chips!")
        elif number == "D3":
            print("You got Water!")
        elif number == "G5":
            print("You got Cola soda!")
        elif number == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid number. Try again.")

vending_machine()







# Friday assignment
import random

def dice_game():
    score = 0
    choice = input("Enter 'r' to roll or 'q' to quit: ").lower()

    while choice == 'r':
        roll = random.randint(1, 7)
        print(f"You rolled: {roll}")

        if roll == 7:
            score += 10
            print("You win! +10 points")
        else:
            score -= 5
            print("You lost! -5 points")

        print(f"Current score: {score}")
        choice = input("Roll again? (r to roll, q to quit): ").lower()

    print(f"Game over! Final score: {score}")