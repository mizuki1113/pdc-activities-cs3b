def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a, b):
    if b == 0:
        return "Error: cannot be divided by zero"
    return a/b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


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
        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation! Please choose: add, subtract, multiply, or divide\n")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if operation == 'add':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}\n")
        elif operation == 'subtract':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}\n")
        elif operation == 'multiply':
            print(f"Result: {num1} × {num2} = {multiply(num1, num2)}\n")
        elif operation == 'divide':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(f"{result}\n")
            else:
                print(f"Result: {num1} ÷ {num2} = {result}\n")

if __name__ == "__main__":
    main()