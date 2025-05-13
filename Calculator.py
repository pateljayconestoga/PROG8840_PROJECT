def add(x, y):
    return x + y

def subtract(x, y):
    # Error introduced: The calculation is done, but the result is not returned.
    # return x - y
    pass # Placeholder to keep the function syntactically valid

def multiply(x, y):
    # Error introduced: The calculation is done, but the result is not returned.
    # return x * y
    pass # Placeholder to keep the function syntactically valid

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    return x / y

def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation_choice():
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            return '+'
        elif choice == '2':
            return '-'
        elif choice == '3':
            return '*'
        elif choice == '4':
            return '/'
        elif choice == '5':
            return 'exit'
        else:
            print("Invalid choice. Please select a valid operation.")

def main():
    print("Welcome to the Simple Calculator!")

    while True:
        operation = get_operation_choice()

        if operation == 'exit':
            print("Exiting calculator. Goodbye!")
            break

        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        result = None # Initialize result

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2) # This will now assign None to result
        elif operation == '*':
            result = multiply(num1, num2) # This will now assign None to result
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Error: Invalid operation."

        if result is None and (operation == '-' or operation == '*'):
            print(f"\nResult: {num1} {operation} {num2} = Error: Function did not return a value (returned None)")
        else:
            print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()