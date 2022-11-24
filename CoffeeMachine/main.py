from data import MENU
from data import resources
from data import coint


def coffee_machine():
    print(MENU)
    print(resources)

    # TODO: 1. Print report of all Coffee Machine resource

    is_continue = True
    resources["money"] = 0

    # Create Check Resource function
    def print_resource():
        print(f'Water: {resources["water"]}')
        print(f'Milk: {resources["milk"]}')
        print(f'Coffee: {resources["coffee"]}')
        print(f'Money: {resources["money"]}')

    def check_resource(type_coffee, drink_type):
        if resources[drink_type] < MENU[type_coffee]["ingredients"][drink_type]:
            return False
        return True

    def is_sales(type_coffee):
        results = {}
        # Check Water
        if not check_resource(type_coffee, "water"):
            results["water"] = {"is_sale": False, "message": "Not enough water"}

        # Check Milk
        if type_coffee == "latte" or type_coffee == "cappuccino":
            if not check_resource(type_coffee, "milk"):
                results["milk"] = {"is_sale": False, "message": "Not enough milk"}

        # Check Coffee
        if not check_resource(type_coffee, "coffee"):
            results["coffee"] = {"is_sale": False, "message": "Not enough coffee"}
        return results

    def check_price(type_coffee, money):
        if money < MENU[type_coffee]["cost"]:
            return False
        return True

    def insert_coin(type_coffee):
        results = {}
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickles = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        money = round(
            quarters * coint["quarters"] + dimes * coint["dimes"] + nickles * coint["nickles"] + pennies * coint[
                "pennies"], 2)
        print(money)
        if not check_price(type_coffee, money):
            results = {"is_sale": False, "message": "Sorry that's not enough money. Money refunded."}
        else:
            if money - MENU[type_coffee]["cost"] >= 0:
                message = f'Pay success, Refund ${round(money - MENU[type_coffee]["cost"], 2)}'
                results = {"is_sale": True, "message": message}
        return results

    def payment(type_coffee):
        # charge resource
        resources["water"] -= MENU[type_coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[type_coffee]["ingredients"]["coffee"]
        if not type_coffee == "espresso":
            resources["milk"] -= MENU[type_coffee]["ingredients"]["milk"]
        # increase money
        resources["money"] += MENU[type_coffee]["cost"]

    while is_continue:
        type_of_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if type_of_coffee == "off":
            is_continue = False
            print("Goodbye see you again.")
        # Print report of all Coffee Machine resource
        elif type_of_coffee == "report":
            print_resource()
        elif type_of_coffee == "espresso" or type_of_coffee == "latte" or type_of_coffee == "cappuccino":
            sale = True
            for key in is_sales(type_of_coffee):
                if not is_sales(type_of_coffee)[key]["is_sale"]:
                    sale = False
                    print(is_sales(type_of_coffee)[key]["message"])
            if sale:
                pay = insert_coin(type_of_coffee)
                if pay["is_sale"]:
                    payment(type_of_coffee)
                print(pay["message"])
        else:
            print("not in list coffee")


# Start Coffee Machine
coffee_machine()
