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


def enough_resources(drinks):
    for item in drinks:
        if resources[item] > drinks[item]:
            return True
        else:
            print(f"Sorry, there is not enough {item}")
            return False


def sum_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def check_transaction(drink_cost, total):
    if total >= drink_cost:
        change = round(total - drink_cost, 2)
        global money
        money += drink_cost
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(choice, drinks):
    for item in drinks:
        resources[item] = resources[item] - drinks[item]
    print(f"Here is your {choice}")





money = 0
machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}g")
        print(f"Money: {money}$")
    else:
        drinks = MENU[choice]
        is_sufficient = enough_resources(drinks["ingredients"])
        if is_sufficient:
            total = sum_coins()
            trans_success = check_transaction(drinks["cost"], total)
            if trans_success:
                make_coffee(choice, drinks["ingredients"])
