import random

def roll_dice():
    count = 0
    while True:
        first_dice = random.randint(1,6)
        second_dice = random.randint(1,6)
        count += 1
        if first_dice != second_dice:
            print (second_dice, first_dice, sep= " : ")
        elif second_dice == first_dice:
            print (second_dice, first_dice, sep= " : ")
            print (count)
            break
        
roll_dice()