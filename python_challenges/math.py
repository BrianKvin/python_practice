def calculate():
    # Ask for input on two numbers and a mathematical operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the mathematical operation (+, -, *, /): ")

    # Perform the operation based on the input
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
            result = "Error: Cannot divide by zero"
    else:
        result = "Invalid operation"

    # Print the result
    print(f"The result of {num1} {operation} {num2} is: {result}")

# Call the function
calculate()

