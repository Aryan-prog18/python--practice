# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

import time
t = time.strftime('%H:%M:%S') # strftime function converts date and time into readable string format
hour = int(time.strftime('%H')) #Here the int function will print the time as integer.
if (hour>=0 and hour<12):
    print("Good Morning sir")
elif (hour>=12 and hour<17):
    print("Good Evening sir")
elif (hour>=17 and hour<0):
    print("Good Night sir")