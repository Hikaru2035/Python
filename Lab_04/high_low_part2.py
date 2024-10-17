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

def play_game():
    print("Card: ")
    card = genarate_card()
    
    while True:
        player = input("Next card higher or lower (higher/lower)?")
        if player == "higher":
            print("Next card is: ")
            next_card = genarate_card()
            if next_card > card:
                print("You won!")
            elif next_card <= card:
                print("You loss!")
            break
        elif player == "lower":
            print("Next card is: ")
            next_card = genarate_card()
            if next_card <= card:
                print("You won!")
            elif next_card > card:
                print("You loss!")
            break
        else:
            print("Enter  valid syntax!")
    
play_game()