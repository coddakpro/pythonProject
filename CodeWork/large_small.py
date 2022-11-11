count = 0
largest_number = 1
smallest_number_int = 0
second_largest_number = 0
while count < 5:
    number_input_int = int(input("Enter your number: "))

    if number_input_int > largest_number:
        second_largest_number = largest_number
        largest_number = number_input_int

    elif number_input_int < smallest_number_int:
        smallest_number_int = number_input_int

    count += 1

print("second_largest", second_largest_number)
print("smallest number ", smallest_number_int)
print("largest_number", largest_number)


