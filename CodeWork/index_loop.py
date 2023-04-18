variable = "Hello boss baby"
print("b" in variable)
for index, letter in enumerate(variable):
    if letter == "b":
        print(letter, " : ", index)
    if letter != "b":
        print(letter)


