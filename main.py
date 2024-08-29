# Menu of available drinks with their ingredients and costs
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
    },
}

# Variable to keep track of the profit made from selling drinks
profit = 0

# Initial resources available in the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Function to check if there are enough ingredients to make the selected drink
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        # Check if the resource is less than the required amount for the drink
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


# Function to process the coins inserted by the user and calculate the total amount
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    # Calculate total money inserted based on coin types
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.001
    return total


# Function to check if the transaction is successful by comparing the money received to the drink's cost
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        # Calculate and print the change to return to the user
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        # Add the cost of the drink to the profit
        profit += drink_cost
        return True
    else:
        # If the money received is not enough, refund it
        print("Sorry, that's not enough money. Money refunded")
        return False


# Function to make the coffee and deduct the ingredients used from the resources
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        # Deduct each ingredient's quantity from the available resources
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} 🍵")


# This variable controls the main loop. If set to False, the machine will stop running.
is_on = True

# Main loop that keeps the coffee machine running
while is_on:
    # Prompt the user for their choice of drink or action
    choice = str(input(
        "What would you like? We have Espresso, Latte or Cappuccino. (Type 'report' to get an update on the balance of ingredients, or 'off' to turn the machine off 😊: ")).lower()

    # If the user types 'off', the machine will turn off (end the loop)
    if choice == "off":
        is_on = False
    # If the user types 'report', print the current resources and profit
    elif choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    # If the user chooses a drink (espresso, latte, or cappuccino)
    else:
        # Get the details of the chosen drink from the menu
        drink = MENU[choice]

        # Check if the resources are sufficient to make the drink
        if is_resource_sufficient(drink["ingredients"]):
            # Process the payment
            payment = process_coins()

            # If the transaction is successful, make the coffee
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
