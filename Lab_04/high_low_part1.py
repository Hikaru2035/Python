import random
def genarate_card():
    card = random.randint(1,13)

    output = [[1, "Ace"],
            [11, "Jack"],
            [12, "Queen"],
            [13, "King"]]

    for num, tag in output:
        if card == num:
            print(tag)
        elif card != num:
            pass
        
    if card in range(2,10):
        print(card)
    
    return card