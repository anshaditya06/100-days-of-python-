import random

# ASCII stages
stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

def print_logo():
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\  
| | | | (_| | | | | (_| | | | | | | (_| | | | | 
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")


def get_random_word(word_list):
    return random.choice(word_list)


def initialize_display(word):
    return ["_"] * len(word)


def display_hangman(lives):
    print(stages[6 - lives])


def process_guess(guess, word, display):
    """
    Returns True if guess is correct, False otherwise
    """
    correct = False
    for i in range(len(word)):
        if word[i] == guess:
            display[i] = guess
            correct = True
    return correct


def play_game():
    word_list = ["ardvark", "baboon", "camel"]
    chosen_word = get_random_word(word_list)
    display = initialize_display(chosen_word)

    guessed_letters = []
    lives = 6
    game_over = False

    print("Welcome to Hangman!")
    print(" ".join(display))
    display_hangman(lives)

    while not game_over:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if not process_guess(guess, chosen_word, display):
            lives -= 1
            print("Wrong guess!")

        display_hangman(lives)
        print(" ".join(display))
        print(f"Lives remaining: {lives}")

        if lives == 0:
            print("You lose! The word was:", chosen_word)
            game_over = True

        if "_" not in display:
            print("You win!")
            game_over = True


# Entry point
print_logo()
play_game()
