print("=== Calculator ===")

while True:
    try:
        a = float(input("Enter the first number: "))
        operation = input("Choose an operation (+, -, *, /): ")
        b = float(input("Enter the second number: "))

        if operation == "+":
            print("Result:", a + b)

        elif operation == "-":
            print("Result:", a - b)

        elif operation == "*":
            print("Result:", a * b)

        elif operation == "/":
            if b == 0:
                print("You cannot divide by 0")
            else:
                print("Result:", a / b)

        else:
            print("Unknown operation")

        again = input("\nDo you want to calculate again? (y/n): ").lower()

        if again != "y":
            print("Program ended")
            break

    except ValueError:
        print("Please enter valid numbers")
