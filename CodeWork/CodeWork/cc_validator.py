user_input = input("Enter your card number for verification: ")
print("######################################################")
print("******************************************************")
print("****Credit Card details:- ", user_input)


def card_length_validity(card_number):
    if card_number > "13" or card_number < "16":
        return "Valid length"
    else:
        return "Invalid length"


print("****Credit Card length:- ", card_length_validity(user_input))


def card_calculator(card_number):
    total_sum_of_even_numbers = 0
    for i in range(len(card_number) - 2, -1, -2):
        sum_of_even_digit = (int(card_number[i]) * 2)
        if sum_of_even_digit > 9:
            sum_sum = (sum_of_even_digit % 10) + (sum_of_even_digit // 10)

            total_sum_of_even_numbers += sum_sum
        else:
            total_sum_of_even_numbers += sum_of_even_digit

    sum_of_odd_digit = 0
    for i in range(len(card_number) - 1, -1, -2):
        sum_of_odd_digit += int(card_number[i])

    if ((total_sum_of_even_numbers + sum_of_odd_digit) % 10) == 0:
        return "Card is valid"
    else:
        return "Card is invalid"


print("****Credit Card Validity:- ", card_calculator(user_input))


def card_type(card_number):
    if card_number[0] == "4":
        return "Visa Card"
    elif card_number[0] == "5":
        return "Master Card"
    elif card_number[0] == "37":
        return "American Express Card"
    elif card_number[0] == "6":
        return "Discover card"
    else:
        return "Invalid Card Type"


print("****Credit Card type:- ", card_type(user_input))
print("******************************************************")
print("######################################################")