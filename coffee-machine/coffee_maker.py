class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"\nWater: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g\n")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕. Enjoy!\n")

    def refill(self):
        print("\nRefilling resources...")
        self.resources["water"] += int(input("Add water (ml): "))
        self.resources["milk"] += int(input("Add milk (ml): "))
        self.resources["coffee"] += int(input("Add coffee (g): "))
        print("Machine successfully refilled!\n")