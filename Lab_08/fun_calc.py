def calc():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Remainder")
    user = int(input("Choose function (1 to 5):"))
    if user == 1:
        print(num1 + num2)
    elif user == 2:
        print(num1 - num2)
    elif user == 3:
        print(num1 * num2)
    elif user == 4:
        print(num1 / num2)
    elif user == 5:
        print(num1 % num2)
    else:
        print("Invalid value!")

calc()