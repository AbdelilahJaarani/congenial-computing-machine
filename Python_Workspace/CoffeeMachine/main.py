MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "money": 0 
} 




def report ():
    print(f"Water: {resources['water']}ml ")
    print(f"Milk: {resources['milk']}ml ")
    print(f"Coffee: {resources['coffee']}g ")
    print(f"Money: ${resources['money']}")




def put_coin():
    quaters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    q = int(input("How many quartes: "))
    d = int(input("How many dimes: "))
    n = int(input("How many nickles: "))
    p = int(input("How many pennies: "))

    quaters *= q  
    dimes  *= d 
    nickles *= n
    pennies *= p
    sum = quaters+dimes+nickles+pennies
    return sum

def checking(waterDr,milkDr,coffeeDr):
   
    if resources ["water"] >= waterDr and resources ["milk"]>= milkDr and resources ["coffee"] >= coffeeDr:
        return True
    elif resources ["water"] < waterDr:
        print("WARNING Not enough Water.")
        ask = input("Do you want to Refill? If yes type 'y' if you the turning off type 'n': ")
        if ask == "y":
          Refill()
        return False
              
    elif resources ["milk"] < milkDr:
        print ("WARNING Not enough Milk.")
        ask = input("Do you want to Refill? If yes type 'y' if you the turning off type 'n': ")
        if ask == "y":
          Refill()
        return False
            
    elif resources ["coffee"] < coffeeDr:
        print ("WARNING Not enought Coffee.")
        ask = input("Do you want to Refill? If yes type 'y' if you the turning off type 'n': ")
        if ask == "y":
          Refill()
        return False
        
        
    
def reduce_water (waterDr):
    resources ["water"] -= waterDr
    return resources ["water"]


def reduce_milk(milkDr):
    resources ["milk"] -= milkDr
    return resources ["milk"]

def reduce_coffee (coffeeDr):
    resources ["coffee"] -= coffeeDr
    return resources ["coffee"]



def refilling_stuff(order,vol):
    resources[order] += vol
    return resources[order]



def Refill():
    command = False 
    while not command:
        ask2 = input ("What do you want to refill? water/milk/coffee: ")
        if ask2 == "water" or ask2 == "milk" or ask2 == "coffee":
            volum = int(input (f"How much of {ask2}: "))
            refilling_stuff(ask2,volum)
            command = True
        else:
            print("Invalid Input")
    
    




def Kaffee(water,milk,coffee,cost):
    if checking(water,milk,coffee) == True:
        money = put_coin()
        if money >= cost:
            reduce_water(water)
            reduce_milk(milk)
            reduce_coffee(coffee)
            money -= cost
            resources["money"] += cost
            return money
        else:
            print("Not enough Money! Money refunded: ")
            return False
    else:
        return False

    
        

def CoffeeMachin():
    turningOFF = False
    while not turningOFF:     
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            turningOFF = True
        elif order == "report":
            report()
        elif order in MENU:
            drink = MENU[order]
            drink_in = drink["ingredients"]
            Rest = Kaffee(drink_in["water"],drink_in["milk"],drink_in["coffee"],drink["cost"])
            if Rest == False:    
                CoffeeMachin()
                break
            print(f"Here is your {order} and the change of: {round(Rest,2)}")
        elif order == "refill":
            Refill()
        else: 
            print ("INPUT INVALID!!")



CoffeeMachin()