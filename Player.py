from Avatar import Avatar
from Item import Item

class Player(Avatar):

    # initalize player variables
    inventory = [] # player inventory
    weapon = "" # might be a dicitonary later storing name : damage stuff

    #initalize constructor
    def __init__(self, _name, _weapon, _hth, _atk, _def):
        super().__init__(_name,_hth,_atk,_def)
        self.weapon = _weapon

    def ItemAdd(self,i):
        print("item added")

    def ItemAdd(self,itemName,itemDescription,itemRange):
        '''Quick function to add items to inventory while adding to the AMOUNT of similar items'''
        print("item created")

        # initalize variables
        newItem = Item(itemName,itemDescription,itemRange,1,None) # new item to be inputted
        foundItem = False # track if item was found or not 

        # Try to find if the item already exists. If add to AMOUNT of that item
        for items in self.inventory:
            currentItemName = self.inventory[self.inventory.index(items)].name

            # ignore case and check if name of both items match
            if(currentItemName.lower() == itemName.lower()):
                # if item already exists add to count
                foundItem = True
                self.inventory[self.inventory.index(items)].amount += 1
                break

        # if the item was never found in the list add to the list
        if(foundItem != True):
            self.inventory.append(newItem)

    def printItems(self):
    
        for items in self.inventory:
            # whole value 
            print(items, "\n")

    def useItem(self, which):
        '''
        which == item use the item range and remove item
        also consider adding an item class which will be able to better point at min max and amount values
        items are complicated right now due to their use of long keys and uncommented embedded lists to match
        dont make program too complicated so maybe consider old system of appending 
        '''

    # toString method 
    def __str__(self):
        return("Hello my name is {}\nI am carrying a {} for a weapon\nHealth: {}\nAttack: {}\nDefense:{}\n\n".format(
            self.name,
            self.weapon,
            self.health,
            self.attack,
            self.defense
            ))

    
    '''
    # initalize possible weapons each weapon has an array with min, max attack values
    wrench = [5.0, 8.0]  # main weapon has attack range of 0.1 to 5
    heat_ray = [0.1, 10]  # was going to be used as alternative stronger weapon ran out of time
    punch = [0.1, 5.0]  # default weapon

    # set the current weapon to use in this case player starts unarmed
    weapon = punch  # current weapon in use
    '''

