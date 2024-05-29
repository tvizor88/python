def calculator():
    while True:
        try:
            print("Enter an operation (+, -, *, /) or 'exit' to end:")
            operation = input()
            if operation == "exit":
                break

            print("Enter the first number:")
            number1 = float(input())
            print("Enter the second number:")
            number2 = float(input())

            if operation == "+":
                result = number1 + number2
            elif operation == "-":
                result = number1 - number2
            elif operation == "*":
                result = number1 * number2
            elif operation == "/":
                result = number1 / number2
            else:
                print("Unknown operation")
                continue

            print("Result: ", result)
        except ValueError:
            print("Please enter a number.")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")
        except Exception as e:
            print("An error occurred:", e)


calculator()
