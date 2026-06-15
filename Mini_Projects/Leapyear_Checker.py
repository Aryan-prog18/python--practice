year = 2000
year1 = 2023
year2 = 2024

if (year %4, year % 100, year%400):
    print("leap year")
else:
    print("not a leap year")

    if (year1 %4, year1 % 100, year1 %400):
        print("Leap year")
    else:
        print("not leap year")

        if (year2 %4, year2 % 100, year2 %400):
            print("Leap year")
        else:
            print("not leap year")