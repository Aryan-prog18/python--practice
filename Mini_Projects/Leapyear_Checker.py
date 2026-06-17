year = 2000
year1 = 2023
year2 = 2024

if (year %4 ==0, year %100 != 0, year %400 == 0):
    print("leap year")
else:
    print("not a leap year")

if (year1 %4 ==0, year1 % 100 != 0, year1 %400 == 0):
     print("Leap year")
else:
    print("not leap year")

if (year2 %4 == 0, year2 % 100 != 0, year2 %400 == 0):
      print("Leap year")
else:
     print("not leap year")