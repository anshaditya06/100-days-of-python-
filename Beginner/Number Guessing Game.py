def clear():
    """Clears the console."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')





def number_guessing_game():
      logo = """
      ╔══════════════════════════════╗
      ║      NUMBER GUESSING GAME    ║
      ╠══════════════════════════════╣
      ║   I'm thinking of a number…  ║
      ║         Can you guess it?    ║
      ╚══════════════════════════════╝
      """
      print(logo)

      levels = {
      "easy": {"range": 10, "attempts": 10},
      "medium": {"range": 50, "attempts": 10},
      "hard": {"range": 100, "attempts": 5}
      }
      
      difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
      if difficulty not in levels:
            print("Invalid difficulty level. Defaulting to easy.")
            difficulty = "easy"

      max_range = levels[difficulty]["range"]
      max_attempts = levels[difficulty]["attempts"]

      import random
      print("Welcome to the Number Guessing Game!")
      print(f"I'm thinking of a number between 1 and {max_range}.")
      number = random.randint(1, max_range)
      attempts = 0
      while True:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > max_range:
                  print(f"Please enter a number between 1 and {max_range}.")
                  continue
            attempts += 1
            if guess < number:
                  print("Too low. Try again.")
            elif guess > number:
                  print("Too high. Try again.")
            else:
                  print(f"Congratulations! You've guessed the number in {attempts} attempts!")
                  input("Press Enter to continue...")
                  clear()
                  break
            if attempts >= max_attempts:
                  print(f"Sorry, you've used all {max_attempts} attempts. The number was {number}.")
                  input("Press Enter to continue...")
                  clear()
                  break

number_guessing_game()

            