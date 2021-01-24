'''
Class for every kind of item including equipment and consumables
this is used to better organize item types as well as names, descriptions
value, and amounts. 

Dictionaries were too small so this is a much better option
'''
class Item:

    # inital attributes 
    name = "" # name of the item 
    description = "" # descriptio n of the item 
    value = 0 # how much of a stat boost this items gives the player
    amount = 0 # how many of the item you have
    iType = "" # if the item is a consumable / armor / weapon
    pickup = False # check if item has already been picked up

    # basic constructor when the player picks up a new item
    def __init__(self, _name, _description, _value, _amount, _iType):
        self.name = _name
        self.description = _description
        self.iType = _iType
        self.value = _value
        self.amount = _amount

    def __str__(self):
        return "Name: {},\nDescription: {},\nValue: {},\nAmount: {}".format(self.name,self.description,self.value,self.amount)
        