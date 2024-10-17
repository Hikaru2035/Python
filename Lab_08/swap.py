def integers(num1, num2):
    list = [num1, num2]
    reversed = list[::-1]
    return reversed

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Before swapping: ", a, b)
    a, b = integers(a, b)
    print("After swapping: ", a, b)

main()