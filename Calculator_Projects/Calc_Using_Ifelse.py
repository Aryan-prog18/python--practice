Operator = input("Enter Operator(+,-,*/):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if Operator == "+":
    print(num1+num2)
elif Operator == "-":
    print(num1-num2)
elif Operator == "*":
    print(num1*num2)
elif Operator == "/":
    print(num1/num2)
else:
    print("Invalid Operator")

