series = []
while len(series)<5:
    input_num = int(input("Enter a number:"))
    series.append(input_num)

total = 0
for each_num in series:
    total +=each_num
    
print("Sum of 5 number is:", total)