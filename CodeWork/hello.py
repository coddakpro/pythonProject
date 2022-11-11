positive_number: int = int(input("Enter a positive number: "))

while positive_number % 2:
    print("Dont be wiser than your destiny")
    positive_number: int = int(input("Enter a positive number: "))
    print("You entered", positive_number)
