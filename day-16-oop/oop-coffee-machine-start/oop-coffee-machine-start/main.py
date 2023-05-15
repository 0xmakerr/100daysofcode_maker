from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_continue = True
coffeemaker = CoffeeMaker()
menu = Menu()
moneymachine = MoneyMachine()

while should_continue:
    choice = input(f"“What would you like? ({menu.get_items()}): ")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        coffeemaker.report()
    else:
        user_drink = menu.find_drink(choice)
        enough_resources = coffeemaker.is_resource_sufficient(user_drink)
        if enough_resources:
            payment = moneymachine.make_payment(user_drink.cost)
            if payment:
                coffeemaker.make_coffee(user_drink)