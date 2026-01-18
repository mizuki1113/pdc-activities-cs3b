def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a * b

def main():
    print("Calculator Program")
    print("\n")
    print("Available operations: add, subtract, multiply, divide")
    print("Type 'stop' to exit the program\n")

    while True:
        operation = input("Enter operation (or 'stop' to quit): ").lower().strip()

        if operation == 'stop':
            print("Thank you for using the calculator. Goodbye!")
            break