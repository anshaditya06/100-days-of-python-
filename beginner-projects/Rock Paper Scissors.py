import random


def clear():
    """Clears the console."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(choices[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw")
        input("Press Enter to continue...")
        clear()
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
        input("Press Enter to continue...")
        clear()
    else:
        print("You lose!")
        input("Press Enter to continue...")
        clear()