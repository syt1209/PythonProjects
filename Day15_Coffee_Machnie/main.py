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

QUARTER = 1/4
DIME = 1/10
NICKEL = 1/20
PENNY = 1/100
machine_on = True
money = 0
sufficient = True


def order():
    return input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")


def sufficient_resources(coffee_choice):
    global sufficient
    coffee_ingredients = MENU[coffee_choice]['ingredients']
    for k, v in coffee_ingredients.items():
        if resources[k] < v:
            print(f"Sorry, there is not enough {k}...")
            return False
        else:
            return True


def coins():
    print("Please insert coins.")
    n_quarters = int(input("how many quarters?: "))
    n_dimes = int(input("how many dimes?: "))
    n_nickles = int(input("how many nickles?: "))
    n_pennies = int(input("how many pennies?: "))
    payment = QUARTER*n_quarters + DIME*n_dimes + DIME*n_dimes + PENNY*n_pennies
    return payment


def transaction(coffee_choice):
    payment = coins()
    cost = MENU[coffee_choice]['cost']
    if payment >= cost:
        change = payment - cost
        print(f"Here is your ${change} in change.")
        make_coffee(coffee_choice)
    else:
        print("Sorry, that's not enough money...")
        print("Money refunded.")


def make_coffee(coffee_choice):
    global money
    coffee_ingredients = MENU[coffee_choice]['ingredients']
    for k, v in coffee_ingredients.items():
        resources[k] -= v
    money += MENU[coffee_choice]['cost']
    print(f"Here is your {coffee_choice} ☕️ Enjoy!")


def coffee_machine():
    global machine_on
    while machine_on:
        choice = order()
        if choice in ["espresso", "latte", "cappuccino"]:
            if sufficient_resources(choice):
                transaction(choice)
            else:
                continue
        if choice == "off":
            print("Coffee machine is turned off...")
            machine_on = False
            break
        if choice == "report":
            report()


coffee_machine()
