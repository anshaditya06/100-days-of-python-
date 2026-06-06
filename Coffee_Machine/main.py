from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

try:
    # Create menu items
    espresso = MenuItem("espresso", 50, 0, 18, 1.5)
    latte = MenuItem("latte", 200, 150, 24, 2.5)
    cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

    MENU = {
        "espresso": espresso,
        "latte": latte,
        "cappuccino": cappuccino,
    }

    # Create machine objects
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            is_on = False

        elif choice == "report":
            coffee_maker.report()
            money_machine.report()

        elif choice == "refill":
            coffee_maker.refill()

        elif choice in MENU:
            drink = MENU[choice]

            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

        else:
            print("Invalid choice.\n")

    while True:
        print("Running...")
except KeyboardInterrupt:
    # This block runs when the interrupt happens
    print("\nIgnoring KeyboardInterrupt... keeping the code running!")
    pass  # 'pass' tells Python to do nothing and continue
