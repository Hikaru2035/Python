def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    print("Welcome to Hangman!")

    # First player enters the word to be guessed
    while True:
        word_to_guess = input("Player 1, enter a word to be guessed: ").lower()

        # Check if the word contains any digits
        if any(char.isdigit() for char in word_to_guess):
            print("Invalid input. Please enter a word without digits.")
        else:
            break

    # Initialize variables
    guessed_letters = set()
    guesses = 0

    print("\nWord to Guess: " + display_word(word_to_guess, guessed_letters))

    while "_" in display_word(word_to_guess, guessed_letters):
        # Second player guesses a letter
        guess = input("Player 2, enter a letter guess: ").lower()

        # Check if the guess is a valid letter
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        guesses += 1

        # Check if the letter has been guessed before
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Update guessed letters
        guessed_letters.add(guess)

        # Display the word with guessed letters
        print("Word to Guess: " + display_word(word_to_guess, guessed_letters))

    print(f"\nCongratulations! You guessed the word '{word_to_guess}' in {guesses} guesses.")


hangman()