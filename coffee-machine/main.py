MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def user_choice():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice


def report():
    for key in resources:
        if key == "water":
            print(f"{key}: {resources[key]}ml")
        if key == "milk":
            print(f"{key}: {resources[key]}ml")
        if key == "coffee":
            print(f"{key}: {resources[key]}g")
    print(f"money: {money}$")


def enough_resources(choice):
    espresso_water = MENU["espresso"]["ingredients"]["water"]
    espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
    latte_water = MENU["latte"]["ingredients"]["water"]
    latte_milk = MENU["latte"]["ingredients"]["milk"]
    latte_coffee = MENU["latte"]["ingredients"]["coffee"]
    cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
    cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
    cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
    if choice == "espresso":
        if resources["water"] - espresso_water >= 0:
            if resources["coffee"] - espresso_coffee >= 0:
                return True, ""
            else:
                return False, "coffee"
        else:
            return False, "water"
    if choice == "latte":
        if resources["water"] - latte_water >= 0:
            if resources["milk"] - latte_milk >= 0:
                if resources["coffee"] - latte_coffee >= 0:
                    return True, ""
                else:
                    return False, "coffee"
            else:
                return False, "milk"
        else:
            return False, "water"
    if choice == "cappuccino":
        if resources["water"] - cappuccino_water >= 0:
            if resources["milk"] - cappuccino_milk >= 0:
                if resources["coffee"] - cappuccino_coffee >= 0:
                    return True, ""
                else:
                    return False, "Coffee"
            else:
                return False, "milk"
        else:
            return False, "water"


def sum_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def check_transaction(total, money):
    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    if choice == "espresso":
        if total < espresso_cost:
            print("Sorry that's not enough money. Money refunded.")
            return money, False
        else:
            if total == espresso_cost:
                money += total
                return money, True
            elif total > espresso_cost:
                money += espresso_cost
                remainder = round(total - espresso_cost, 2)
                print(f"Here is ${remainder} dollars in change.")
                return money, True
    elif choice == "latte":
        if total < latte_cost:
            print("Sorry that's not enough money. Money refunded.")
            return money, False
        else:
            if total == latte_cost:
                money += total
                return money, True
            elif total > latte_cost:
                money += latte_cost
                remainder = round(total - latte_cost, 2)
                print(f"Here is ${remainder} dollars in change.")
                return money, True
    elif choice == "cappuccino":
        if total < cappuccino_cost:
            print("Sorry that's not enough money. Money refunded.")
            return money, False
        else:
            if total == cappuccino_cost:
                money += total
                return money, True
            elif total > cappuccino_cost:
                money += cappuccino_cost
                remainder = round(total - cappuccino_cost, 2)
                print(f"Here is ${remainder} dollars in change.")
                return money, True


def make_coffee(choice, resources, MENU):
    if do_check_transaction == True and is_enough_resources == True:
        if choice == "espresso":
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            print(f"Here is your {choice}. Enjoy!")
            return resources
        elif choice == "latte":
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            print(f"Here is your {choice}. Enjoy!")
            return resources
        elif choice == "cappuccino":
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            print(f"Here is your {choice}. Enjoy!")
            return resources
    else:
        return resources

money = 0
machine_on = True
while machine_on:
    choice = user_choice()

    if choice == "report":
        report()
    elif choice == "off":
        machine_on = False
    else:
        is_enough_resources, no_resources = enough_resources(choice)
        if is_enough_resources == False:
            print(f"Sorry, not enough {no_resources}")
        else:
            total = sum_coins()
            money, do_check_transaction = check_transaction(total, money)
            resources = make_coffee(choice, resources, MENU)