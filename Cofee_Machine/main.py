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

COINS = {
    "quarters" : 0.25 ,
    "dimes" : 0.10 ,
    "nickles" : 0.05 ,
    "pennies" : 0.01
    }


PROFIT = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_coins():
    mony = 0
    print("Please insert coins.")
    for key,value in COINS.items():
        coin = int(input(f"How many {key}?: "))
        mony += coin*value
    return mony



         
         

def get_resources():
    for key,value in resources.items():
        if key == "coffee":
            print(f"{key} : {value}g")
        else:
            print(f"{key} : {value}ml")
    print(f"Mony : ${PROFIT}")
    


def get_menu_items():
    items = []
    for item in MENU:
        items.append(item)
    return items


def is_resources_sufficent(order_ingredient):
    for key,value in order_ingredient.items():
        if value >= resources[key]:
            print(f"sorry ther is not enough {key}")
            return False
    return True


def is_transaction_successful(mony_recived , drink_cost):
    if mony_recived >= drink_cost:
        change = round(mony_recived - drink_cost , 2)
        print(f"Here is ${change} in change")
        global PROFIT
        PROFIT += drink_cost
        return True
    else:
        print("Sorry that`s not enough mony. Mony refunded.")
        return False

def make_coffee(drink_name , order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} Enjoy ♥")
    

          
def check_answers():
    should_continue = True
    while should_continue:
        guess = input(f"what would you like? {get_menu_items()}: ").lower()
        if guess == "report":
            get_resources()
        elif guess in get_menu_items():
            if is_resources_sufficent(MENU[guess]["ingredients"]):
                user_pay = get_coins()
                if is_transaction_successful(user_pay , MENU[guess]["cost"]):
                    make_coffee(guess , MENU[guess]["ingredients"])
                    


check_answers()
    
