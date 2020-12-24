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


def check_resources(coffee_flavor, ingredient):
    ingredient_remain = resources[ingredient]
    ingredient_require = MENU[coffee_flavor]["ingredients"][ingredient]
    # print(f"{ingredient} req: {ingredient_require}, remain: {ingredient_remain}")
    if ingredient_require > ingredient_remain:
        return False
        # return f"Sorry, {ingredient} is not enough to make {coffee_flavor}"
    else:
        return True


# def report(water_remain,milk_remain,coffee_remain,money_remain):
def report():
    print(f"Water: {water_remain}ml \nMilk: {milk_remain}ml \nCoffee: {coffee_remain}g \nMoney: ${money_remain}")


turn_off_machine = False
resources["money"] = 0.0

while not turn_off_machine: 
    water_remain = resources["water"]
    milk_remain = resources["milk"]
    coffee_remain = resources["coffee"]
    money_remain = resources["money"]

    coffee_flavor = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_flavor == "espresso":
        MENU[coffee_flavor]["ingredients"]["milk"] = 0

    if coffee_flavor == "off":
        turn_off_machine = True
        print("Turning off coffee machine...")
    elif coffee_flavor == "report":
        report()
        # check_resources()
    else:
        water_req = MENU[coffee_flavor]["ingredients"]["water"]
        milk_req = MENU[coffee_flavor]["ingredients"]["milk"]
        coffee_req = MENU[coffee_flavor]["ingredients"]["coffee"]
        money_req = MENU[coffee_flavor]["cost"]

        # print(f"water: {water_req}, milk: {milk_req}, Coffee: {coffee_req}, Money: {money_req}")

        if not check_resources(coffee_flavor, "water"):
            print(f"Sorry, water is not enough to make {coffee_flavor}")
            turn_off_machine = True
        elif not check_resources(coffee_flavor, "milk"):
            print(f"Sorry, milk is not enough to make {coffee_flavor}")
            turn_off_machine = True
        elif not check_resources(coffee_flavor, "coffee"):
            print(f"Sorry, coffee is not enough to make {coffee_flavor}")
            turn_off_machine = True
        else:
            # get inputs for the coins
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            amount_paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
            # check whether the money is enough
            if money_req > amount_paid:
                # if it is not enough quit program
                print("Sorry that's not enough money. Money refunded.")
                turn_off_machine = True
            else:
                # if it is enough, return the change and process further
                resources["money"] += money_req
                resources["water"] -= water_req
                resources["milk"] -= milk_req
                resources["coffee"] -= coffee_req
                refund_money = round(amount_paid - money_req, 2)
                print(f"Here is ${refund_money} in change.")
                # update money in ledger
                print(f"Your {coffee_flavor} is ready! Enjoy!")
