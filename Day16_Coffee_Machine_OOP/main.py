from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffees = coffee_menu.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_on = True
while machine_on:
    order = input(f"What would you like? {coffees}\n")
    if order == "off":
        machine_on = False
    elif order == "report":
        coffee_maker.report()
    else:
        coffee = coffee_menu.find_drink(order)
        if coffee is not None:
            can_make = coffee_maker.is_resource_sufficient(coffee)

            if can_make:
                payment_successful = money_machine.make_payment(coffee.cost)
                if payment_successful:
                    coffee_maker.make_coffee(coffee)
