name = "Aliyah"
age = 18
print(name, "is", age, "years old")
s = "{1} is {0:-^10} years old".format(age, name)
print(s)
hello = "hello world"
for index, letter in enumerate(hello):
    print(f"{letter} --> {index}")

    for i in range(1, 21, 2):
        s = "*" * i
        print(f"{s:20}{s:<20}{s:^20}{s:>20}")
