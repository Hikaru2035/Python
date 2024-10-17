total_pos=0
total_neg=0
number_of_neg = 0
number_of_pos = 0

for total in range (10) :
    total = int(input("Enter number: "))
    if total < 0:
        total_neg += total
        number_of_neg += 1
    elif total >= 0:
        total_pos += total
        number_of_pos += 1

if number_of_neg == 0:
    print("No negative number")
else:
    print(round(total_neg/number_of_neg,2))
    print(total_neg)
    
if number_of_pos == 0:
    print("No positive number")
else:
    print(round(total_pos/number_of_pos,2))
    print(total_pos)

