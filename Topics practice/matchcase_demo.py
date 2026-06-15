op = input("Enter operator: ")
num = int(input("Enter a number: "))
num1 = int(input("Enter another number: "))
match op:
    case "+":
        print(num+num1)
    case "-":
        print("Subtraction")
    case "/":
        print("Division")
    case "*":
        print("Multiplication")
    case _:
        print("Invalid Operator")
