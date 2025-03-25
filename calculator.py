def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %")

    # Get user input
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            result = "Error! Modulo by zero."
    else:
        result = "Invalid operation!"

    # Display result
    print(f"Result: {result}")

# Run the calculator
calculator()
