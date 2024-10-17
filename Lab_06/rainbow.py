mylist = [[1, "Red"],
        [2, "Orange"],
        [3, "Yellow"],
        [4, "Green"],
        [5, "Blue"],
        [6,"Indigo"],
        [7, "Violet"]]

while True:
    user = int(input("Enter a number:"))
    for num, color in mylist:
        if user == num:
            print(color)
        elif user != num:
            pass

    if user == -1:
        break
    else:
        print("Invalid input!")
