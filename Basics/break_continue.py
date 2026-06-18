while True:
    num = int(input("Enter The Number: "))
    if (num <= 0):
        print("Invalid Input, Try again")
        continue # if user enter invalid num so it will go back to the while loop and start again
    for i in range(11):
        print(num, "x", i, "=", num *(i))
        if (i == 10):
            break

#! Here I used combination of functions to make this table generator
# !-- Used while loop
# !-- Used for loop 
# !-- Used break and continue function