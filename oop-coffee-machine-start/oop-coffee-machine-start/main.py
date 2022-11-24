from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
money = 0
is_continue = True
while is_continue:
    # TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    choose = input("What would you like? (espresso/latte/cappuccino/):")

    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
    if choose == "off":
        is_continue = False
        print("Good bye.")
    # TODO 3: Print report
    elif choose == 'report':
        coffee_maker.report()
        money_machine.report()

    # TODO 4: Check resources sufficient?
    else:
        drink = menu.find_drink(choose)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # TODO 5: Process coins.
            # TODO 6: Check transaction successful?
            # TODO 7: Make Coffee.
            coffee_maker.make_coffee(drink)









