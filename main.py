try:

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("What operation would you like to perform?\n 1.Press + for Addition\n 2. Press - for Subtraction\n 3. Press * for Multiplication\n 4. Press / for Division")

    o = input("Enter your operation: ")
    match o:
        case "+":
            print(f"The result of {a} + {b} is: {a + b}")
        case "-":
            
            print(f"The result of {a} - {b} is: {a - b}")
        case "*":
            print(f"The result of {a} * {b} is: {a * b}")
        case "/":
            if b != 0:
                print(f"The result of {a} / {b} is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please choose a valid operation.")
except ValueError:
    print("Please enter valid numbers.")
