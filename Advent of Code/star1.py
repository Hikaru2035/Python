def total_num():
    file1 = open("input1.txt","r")
    count = 0
    total = 0
    for line in file1:
        list =[]
        for x in line.strip():
            try:
                x = int(x)
                list.append(x)
            except ValueError:
                pass  # it was a string, not an int.  
        number = int(str(list[0])+str(list[-1]))
        print("Line{}: {}".format(count, line.strip()))
        print(number)
        total += number
        count += 1
    return total

print(total_num())
        