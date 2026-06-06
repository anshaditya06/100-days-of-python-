logo = '''
██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗ 
██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗
███████║██║██║  ███╗███████║█████╗  ██████╔╝
██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗
██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
'''
print(logo)

data = [
    {"name": "Elon Musk", "description": "CEO of Tesla and SpaceX", "net_worth": 240},
    {"name": "Jeff Bezos", "description": "Founder of Amazon", "net_worth": 170},
    {"name": "Bernard Arnault", "description": "Chairman of LVMH", "net_worth": 210},
    {"name": "Bill Gates", "description": "Co-founder of Microsoft", "net_worth": 120},
    {"name": "Mark Zuckerberg", "description": "CEO of Meta", "net_worth": 140},
    {"name": "Larry Ellison", "description": "Co-founder of Oracle", "net_worth": 135},
    {"name": "Warren Buffett", "description": "Chairman of Berkshire Hathaway", "net_worth": 115},
    {"name": "Larry Page", "description": "Co-founder of Google", "net_worth": 125},
    {"name": "Sergey Brin", "description": "Co-founder of Google", "net_worth": 120},
    {"name": "Steve Ballmer", "description": "Former CEO of Microsoft", "net_worth": 110},
    {"name": "Mukesh Ambani", "description": "Chairman of Reliance Industries", "net_worth": 105},
    {"name": "Gautam Adani", "description": "Founder of Adani Group", "net_worth": 95},
    {"name": "Michael Bloomberg", "description": "Founder of Bloomberg LP", "net_worth": 90},
    {"name": "Carlos Slim", "description": "Chairman of Grupo Carso", "net_worth": 85},
    {"name": "Francoise Bettencourt Meyers", "description": "L'Oreal heiress", "net_worth": 100},
    {"name": "Amancio Ortega", "description": "Founder of Zara", "net_worth": 80},
    {"name": "Alice Walton", "description": "Walmart heiress", "net_worth": 70},
    {"name": "Jim Walton", "description": "Walmart heir", "net_worth": 72},
    {"name": "Rob Walton", "description": "Walmart heir", "net_worth": 68},
    {"name": "MacKenzie Scott", "description": "Philanthropist and author", "net_worth": 45}
]


def clear():
    #Clears the console
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


import random
def get_random_person():
    """Get data from random account"""
    return random.choice(data)

def format_person(person):
    return f"{person['name']}, a {person['description']}"


def check_answer(user_guess, a_worth, b_worth):
    if a_worth > b_worth:
        return user_guess == "a"
    else:
        return user_guess == "b"


def play_game():
    score = 0
    game_should_continue = True

    person_a = get_random_person()
    person_b = get_random_person()

    while game_should_continue:
        print(f"\nCompare A: {format_person(person_a)}")
        print("VS")
        print(f"Against B: {format_person(person_b)}")

        guess = input("Who has higher net worth? Type 'A' or 'B': ").lower()

        a_worth = person_a["net_worth"]
        b_worth = person_b["net_worth"]

        is_correct = check_answer(guess, a_worth, b_worth)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            person_a = person_b
            person_b = get_random_person()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == 'y':
                clear()
                print(logo)
                play_game()
            else:
                print("Thanks for playing!")
                clear()
                print(logo)




play_game()