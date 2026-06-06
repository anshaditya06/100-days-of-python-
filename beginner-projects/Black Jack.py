def clear():
    """Clears the console."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
      """Prints the logo of the game."""
      print(r""" 
             ╔══════════════════════════════════╗
            ║   ♠  ♥   B L A C K J A C K   ♦  ♣   ║
             ╚══════════════════════════════════╝

        ┌─────────┐   ┌─────────┐
        │ A       │   │ K       │
        │    ♠    │   │    ♥    │
        │       A │   │       K │
        └─────────┘   └─────────┘
      """)




def deal_cards():
    """Returns a list of 2 random cards from the deck."""
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over 21. You lose"
    elif c_score > 21:
        return "Opponent went over 21. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
      use_cards = []
      computer_cards = []
      computer_score = -1
      user_score = -1

      game_over = False

      for _ in range(2):
            use_cards.append(deal_cards())
            computer_cards.append(deal_cards())



      while not game_over:
            user_score = calculate_score(use_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {use_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
            if user_score == 0 or computer_score == 0 or user_score > 21:
                        game_over = True
            else:
                        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                        if user_should_deal == "y":
                              use_cards.append(deal_cards())
                        else:
                              game_over = True

      while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_cards())
            computer_score = calculate_score(computer_cards)
      
      print(f"Your final hand: {use_cards}, final score: {user_score}")
      print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")    
      print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
      clear()
      logo()
      play_game()