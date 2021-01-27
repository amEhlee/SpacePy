from Avatar import Avatar
from Item import Item
import math

class Player(Avatar):    

    ''' POSSIBLE INVSERTIONS
    # initalize possible weapons each weapon has an array with min, max attack values
    wrench = [5.0, 8.0]  # main weapon has attack range of 0.1 to 5
    heat_ray = [0.1, 10]  # was going to be used as alternative stronger weapon ran out of time
    punch = [0.1, 5.0]  # default weapon

    # set the current weapon to use in this case player starts unarmed
    weapon = punch  # current weapon in use
    '''

    # initalize player variables
    inventory = [] # player inventory

    # More on stats -///-: possible move to avatar class?
    weaponName = "" # might be a dicitonary later storing name : damage stuff
    weaponValues = None # damage range for weapon -///-: rennovated into inventory like system later?
    ArmorName = "" # might be a dicitonary later storing name : damage stuff
    ArmorValues = None # damage range for weapon -///-: rennovated into inventory like system later?


    #initalize constructor
    def __init__(self, _name, _weapon, _hth, _atk, _def):
        super().__init__(_name,_hth,_atk,_def)
        self.weapon = _weapon

    '''
        REGION: ITEMS AND STATS
    '''
    #-///-:
    def ItemAdd(self,itemName,itemDescription,itemRange):
        '''Quick function to add items to inventory while adding to the AMOUNT of similar items'''

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

    def useItem(self, itemName):
        '''
        which == item use the item range and remove item
        also consider adding an item class which will be able to better point at min max and amount values
        items are complicated right now due to their use of long keys and uncommented embedded lists to match
        dont make program too complicated so maybe consider old system of appending 
        '''
        # If item is found in table buff player and decrease amount of item
        for items in self.inventory:
            currentItemName = self.inventory[self.inventory.index(items)].name

            # ignore case and check if name of both items match
            if(currentItemName.lower() == itemName.lower()):
                # if item already exists decrease count and use the item
                foundItem = self.inventory[self.inventory.index(items)]
                foundItem.amount -= 1

                # apply the item to play stats
                applyItem(foundItem)

                # Check if we ran out of that item
                if(foundItem.amount == 0):
                    # if so remove it from list 
                    self.inventory.remove(foundItem)

                # We're done here. Break outta the loop
                break

    def applyItem(self,item):
        # check if its armor 
        if(item.type == "armor"):
            self.armorName = item.name
            self.armorValues = item.value
        # check if its a weapon
        elif(item.type == "weapon"):
            self.weaponName = item.name
            self.weaponValues = item.value
        # check if its a consumable -///-: ignore case
        elif(item.type == "consumable"):
            # only healing items for now so ill just factor for those
            # calculate how much to heal the player for 
            amount = math.uniform(item.value[0], item.value[1])

            # add to player health by certain amount #VALUES should be between min and max ranges specified in values list per item 
            self.health += amount * 10

            # return a message indictating health             
            print('This action has %s points' % amount)
        

    def printItems(self):
        '''Quick function that iterates through and prints all items and equipment in inventory'''
        print("--------------ITEMS--------------")

        # check if user has items
        if(not self.inventory):
            # no items? print this
            print("You have no items in your inventory")
        else:
            # items? print this 
            for items in self.inventory:
                print(items, "\n")
                print("----------------------------")

    '''
        END REGION ITEMS AND STATS
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
