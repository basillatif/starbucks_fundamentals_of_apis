from datetime import datetime
from flask import make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
COFFEE = {
    "Latte": {
        "coffee_name": "Latte",
        "milk": "Whole",
        "timestamp": get_timestamp()
    },
    "Cappuccino": {
        "coffee_name": "Cappuccino",
        "milk": "Oat",
        "timestamp": get_timestamp()
    },
    "Flat White": {
        "coffee_name": "FlatWhite",
        "milk": "Soy",
        "timestamp": get_timestamp()
    }
}

# Create a handler for coffee get route
def read():
    """
    This function responds to a request for /api/coffee
    with the complete lists of coffee drinks
    """
    # Create the list of coffee from our data
    return [COFFEE[key] for key in sorted(COFFEE.keys())]

def create(coffee):
    """
    This function creates a new drink in the coffee object
    :param coffee:  coffee drink to create
    :return:        201 on success, 406 if drink exists
    """
    coffee_name = coffee.get("coffee_name", None)
    milk = coffee.get("milk", None)
    """
    Generator expression inside the any() function to iterate over the values 
    of the dictionary and check if the "milk" value of any of the inner dictionaries 
    is equal to the provided value. If the any() function returns False, it means that the provided value was not found in any of the nested dictionaries, 
    so the print statement will be executed.
    """
    if not any(milk_name['milk'] == milk for milk_name in COFFEE.values()):
        COFFEE[coffee_name] = {
            "coffee_name": coffee_name,
            "milk": milk,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{coffee_name} successfully created".format(coffee_name=coffee_name), 201
        )
    else:
        abort(
            406,
            "Milk, {milk}, already exists".format(milk=milk),
        )      