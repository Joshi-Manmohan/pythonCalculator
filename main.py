operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator."

print(result)
