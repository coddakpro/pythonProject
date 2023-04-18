try:
    file_name = open("path", "w")
    file_name.write("Hello")
except IOError:
    print("cannot write to a closed file")
else:
    file_name.close()
    print("sentence to Death")