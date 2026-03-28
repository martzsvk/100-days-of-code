from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# class for coffees
class MenuItem:
    def __init__(self,name,cost,ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients

espresso = MenuItem("espresso", 1.5, {"water": 50, "coffee": 18})
latte = MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24})
cappuccino = MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24})

# while loop
working = True
while working:
    # asking user what coffee he wants
    ask = input(f"What would you like? ({menu.get_items()}): ")

    # espresso
    if ask == espresso.name:
        menu.find_drink(espresso.name)
        # there must be enough resources
        if coffee_maker.is_resource_sufficient(espresso):
            # if there's enough resources - checking if user inputs enough money
            if money_machine.make_payment(espresso.cost):
                # if everything is passed - make coffee 
                coffee_maker.make_coffee(espresso)

    # latte
    if ask == latte.name:
        menu.find_drink(latte.name)
        if coffee_maker.is_resource_sufficient(latte):
            if money_machine.make_payment(latte.cost):
                coffee_maker.make_coffee(latte)

    # cappuccino
    if ask == cappuccino.name:
        menu.find_drink(cappuccino.name)
        if coffee_maker.is_resource_sufficient(cappuccino):
            if money_machine.make_payment(cappuccino.cost):
                coffee_maker.make_coffee(cappuccino)

    # report of ingredients and money
    if ask == "report":
        coffee_maker.report()
        money_machine.report()

    # turning off the machine
    if ask == "off":
        working = False









