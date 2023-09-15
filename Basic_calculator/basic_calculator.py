def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

choice = input("What operation do you want to perform? (add, subtract, multiply, divide) ")

if choice == "add":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(add(a, b))
elif choice == "subtract":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(subtract(a, b))
elif choice == "multiply":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(multiply(a, b))
elif choice == "divide":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(divide(a, b))
else:
    print("Invalid choice")
