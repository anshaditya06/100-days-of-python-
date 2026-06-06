class MoneyMachine:
    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: ${self.profit}\n")

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("How many quarters? ")) * 0.25
        total += int(input("How many dimes? ")) * 0.10
        total += int(input("How many nickels? ")) * 0.05
        total += int(input("How many pennies? ")) * 0.01
        return total

    def make_payment(self, cost):
        money_received = self.process_coins()
        if money_received >= cost:
            change = round(money_received - cost, 2)
            print(f"Here is ${change} in change.")
            self.profit += cost
            return True
        else:
            print("Sorry that's not enough money. Money refunded.\n")
            return False