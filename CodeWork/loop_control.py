count = 0
largest_number = 0
while count > 5:
    number = int(input("Give me a number: "))
    if number > largest_number:
        largest_number = number

    count += 1
print("The largest number is: ", largest_number)
