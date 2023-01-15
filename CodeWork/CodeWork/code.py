import time

time_string = "22 january, 2020"
print("string representing time:", time_string)
result = time.strptime(time_string, "%d %b %y")
print(result)
time_string = "30 Nov 00"
print("\nString representing time:", time_string)
result = time.strptime(time_string, "%d %b %y")
print(result)
time = '04/11/15 11:55:23'
print("\nString representing time:", time_string)
result = time.strptime(time_string, "%m/%d/%y%H:%M:%S")
print(result)
time_string = '12-11-2019'
print("\nString representing:", time_string)
result = time.strptime(time_string, "%m-%d-%Y")
print(result)
time_string = '13::55::26'
print("\nString representing time:", time_string)
result = time.strptime(time_string, "%H::%M::%S")
print(result)
