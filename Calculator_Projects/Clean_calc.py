'''Calculator using built in functions'''

import operator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
Op = input("Enter a Operator: ")
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod

}

result = operations[Op](num1,num2)
print(result)