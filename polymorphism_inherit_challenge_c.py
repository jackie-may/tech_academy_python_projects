

#parent class beverage
class Beverage:
    name = "beverage"
    color = "clear"
    amount = None
    available = True

    #method in the parent class
    def information(self):
        entry_name = input("enter the name of the beverage here: ")
        entry_amount = input("enter the amount of beverage that you would like here: ")
        if (entry_name == "water"):
            print("Great! It is available!")
        else:
            print("That beverage is unavailable at the moment :(")

    #child class #1 water
class Water(Beverage):
    #inherited and polymorphed attributes
    name = "water"
    color = "clear"
    amount = 32
    available = True
    #unique attributes to this child class
    alcoholic = False
    composition = "H20"

#child class #2 soda
class Soda(Beverage):
    #inherited and polymorphed attributes
    name = "soda"
    color = "brown"
    amount = None
    available = False
    #unique attributes to this child class
    calories = 120
    carbonated = True
        
        
available_drinks = Beverage()
available_drinks.information()
