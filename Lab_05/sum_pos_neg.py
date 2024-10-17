total_pos=0
total_neg=0
for total in range (10) :
    total = int(input("Enter number: "))
    if total < 0:
        total_neg += total
    elif total >= 0:
        total_pos += total
print(total_neg)
print(total_pos)
    