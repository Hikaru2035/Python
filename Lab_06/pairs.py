import random

def initialize_board():
    cards = ["Jack", "Queen", "King", "Ace"]
    deck = cards * 4
    random.shuffle(deck)
    
    board = [["*" for _ in range(4)] for _ in range(4)]
    
    for row in range(4):
        for col in range(4):
            card = deck.pop()
            board[row][col] = card
    
    return board

def display_board(board):
    print("   0 1 2 3")
    for row in range(4):
        print(f"{row} ", end=" ")
        for col in range(4):
            if board[row][col] == '*' or board[row][col] == 'X':
                print(board[row][col], end=" ")
            else:
                print('*', end=" ")
        print()

def get_card_position():
    try:
        row = int(input("Enter the row for the card: "))
        col = int(input("Enter the column for the card: "))
        return row, col
    except ValueError:
        print("Invalid input. Please enter integers.")
        return get_card_position()

def play_game():
    board = initialize_board()
    matched_pairs = set()

    print("Initial Board:")
    display_board(board)
    
    while len(matched_pairs) < 16:
        print("\nEnter card positions (row column):")

        row1, col1 = get_card_position()
        card1 = board[row1][col1]
        print(f"Card at position {row1} {col1}: {card1}")

        row2, col2 = get_card_position()
        card2 = board[row2][col2]
        print(f"Card at position {row2} {col2}: {card2}")

        if card1 == card2 and (row1, col1) not in matched_pairs and (row2, col2) not in matched_pairs:
            print("Matching pair!")
            matched_pairs.add((row1, col1))
            matched_pairs.add((row2, col2))
            
            # Update the game grid with 'X' at the positions of the matching pair
            board[row1][col1] = 'X'
            board[row2][col2] = 'X'
        else:
            print("Not a matching pair. Try again.")

        # Display the updated game board
        display_board(board)

    print("\nCongratulations! You found all the pairs.")
play_game()