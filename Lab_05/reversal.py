while True:
    num = int(input("Enter an iinterger of at least 2 digits or -1 to quit:"))
    if num == -1:
        print("Program end.")
        break
    elif num in range (9,100000000000):
        print(str(num)[::-1])
    else:
        print("Your input is invalid, please try again.")
