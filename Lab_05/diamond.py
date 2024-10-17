target = int(input("Enter a number"))
for count in range(target):
    print(' '*(target-count-1) + '* '*(count+1) )
for count in range(target):
    print(' '*(count+1) + '* '*(target-count-1))