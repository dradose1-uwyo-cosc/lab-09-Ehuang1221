# Edmon Huang
# UWYO COSC 1010
# Submission Date: 11/12/2024
# Lab 09
# Lab Section: 11
# Sources, people worked with, help given to:
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.


# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""

class Pizza:
    def __init__(self, size, sauce = "red"): # constructor for Pizza class
        self.size = size if size >= 10 else 10 # makes sure size is at least 10
        self.sauce = sauce # initializes the sauce attribute 
        self.toppings = ["cheese"] # initializes the toppings list with cheese

    def getSize(self): # returns size attribute
        return self.size 
    
    def setSize(self, size): # sets size attribute 
        if size >= 10: # must be greater than or equal to 10
            self.size = size # sets size if greater than 10
        else:
            self.size = 10 # if less than 10 sets to 10
    
    def getSauce(self):
        return self.sauce # returns sauce attribute

    def getToppings(self):
        return self.toppings # returns toppings list 
    
    def setToppings(self, *new_toppings): # Defines method allowing multiple toppings to be added
        for topping in new_toppings: # Loops through each topping in new_toppings
            self.toppings.append(topping) # appends each topping to the list
    
    def getAmountOfToppings(self):
        return len(self.toppings) # returns the length of toppings list
    
class Pizzeria: # Pizza class
    price_per_topping = 0.30
    price_per_inch = 0.60

    def __init__(self): # Constructor for Pizzeria Class 
        self.orders = 0 # Tracks orders placed
        self.pizzas = [] # Initializes pizza list
    
    def placeOrder(self): # Defines method to store orders
        self.orders += 1 # Increments orders
        size = int(input("Please enter the size of the pizza as a whole number (smallest is 10): "))
        sauce = input("What kind of sauce would you like?\nLeave blank for red sauce: ").strip()
        if not sauce: # if empty string, sauce is red
            sauce = "red"
        
        pizza = Pizza(size, sauce) # Creates object using size and sauce

        print("Please enter toppings you would like, leave blank and enter when done.")
        while True: # Repeated prompts topping input
            topping = input()
            if topping == "":
                break
            pizza.setToppings(topping) # adds topping to pizza object's topping list

        self.pizzas.append(pizza) # adds pizza to pizza list

    def getPrice(self): 
        pizza = self.pizzas[-1] # Gets most recent pizza added to list
        base_price = pizza.getSize() * self.price_per_inch # gets base price of pizza
        topping_price = (pizza.getAmountOfToppings() - 1) * self.price_per_topping  # gets topping price minus one to exclude cheese
        total_price = base_price + topping_price
        return base_price, topping_price, total_price # Returns all three prices
    
    def getReceipt(self): 
        pizza = self.pizzas[-1] # Gets most recent pizza
        base_price, topping_price, total_price = self.getPrice() # Gets prices from getPrice()

        print(f"\nYou ordered a {pizza.getSize()}\" pizza with {pizza.getSauce()} sauce and the following toppings:")
        for topping in pizza.getToppings():
            print(f"    {topping}")
        print(f"\nYou ordered a {pizza.getSize()}\" pizza for ${base_price:.2f}")
        print(f"You had {pizza.getAmountOfToppings() - 1} topping(s) for ${topping_price:.2f}")
        print(f"Your total price is ${total_price:.2f}")

    def getNumberOfOrders(self):
        return self.orders

# Main program logic
pizzeria = Pizzeria()

while True:
    order_prompt = input("Would you like to place an order? Type 'exit' to quit: ").strip().lower()
    if order_prompt == "exit":
        break
    pizzeria.placeOrder()
    pizzeria.getReceipt()

print(f"\nTotal number of orders placed: {pizzeria.getNumberOfOrders()}")








            

