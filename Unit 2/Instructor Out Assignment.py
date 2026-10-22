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