import random
 
# Function to initialize the game grid with a destroyer
def initialize_grid():
    grid = [['[ ]' for _ in range(5)] for _ in range(5)]
    orientation = random.choice(['horizontal', 'vertical'])
    row = random.randint(0, 4)
    col = random.randint(0, 3) if orientation == 'horizontal' else random.randint(0, 4)
   
    if orientation == 'horizontal':
        grid[row][col] = '[D]'
        grid[row][col + 1] = '[D]'
    else:
        grid[row][col] = '[D]'
        grid[row + 1][col] = '[D]'
 
    return grid
 
# Function to display the game grid with indices
def display_grid(grid):
    print("    0   1   2   3   4")
    for i, row in enumerate(grid):
        print(f"{i}  {' '.join([cell if cell in ('[H]', '[M]') else '[ ]' for cell in row])}")
    print()
 
# Function to check if a shot is a hit or a miss
def check_shot(grid, row, col):
    if grid[row][col] == '[D]':
        grid[row][col] = '[H]'  # Hit
        return True
    else:
        grid[row][col] = '[M]'  # Miss
        return False
 
# Main game loop
def play_game():
    game_grid = initialize_grid()
 
    while '[D]' in [cell for row in game_grid for cell in row]:
        display_grid(game_grid)
        try:
            guess_row = int(input("Enter row (0-4): "))
            guess_col = int(input("Enter column (0-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
 
        if 0 <= guess_row <= 4 and 0 <= guess_col <= 4:
            if check_shot(game_grid, guess_row, guess_col):
                print("Hit!")
            else:
                print("Miss!")
        else:
            print("Invalid input. Please enter a number between 0 and 4.")
 
    display_grid(game_grid)
    print("Congratulations! You sank the destroyer.")
 
# Run the game
play_game()