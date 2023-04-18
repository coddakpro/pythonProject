def error_handle():
    try:
        file_name = open("C:\\User\\user\\Documents\\free universities.txt", "r")
        print(file_name.read(10))
    except IOError as e:
        print("can not write to it", e)
    else:
        file_name.close()
        print("file closed successfully")