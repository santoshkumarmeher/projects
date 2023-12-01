from arts import calculator
print(calculator)


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


def aam(a, b):
    return a % b


first_number=int(input("Enter first number: "))
second_number=int(input("Enter Second Number: "))
operation=input("Which operation do you want to perform '+','-','*','/','%' :  ")

if operation == "+":
    print(add(first_number, second_number))
elif operation == "-":
    print(sub(first_number, second_number))
elif operation == "*":
    print(mul(first_number, second_number))
elif operation == "/":
    print(div(first_number, second_number))
elif operation == "%":
    print(aam(first_number, second_number))
else:
    print("Invalid operation!!!...")

