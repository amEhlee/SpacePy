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
    currentWeapon = None;


    #initalize constructor
    def __init__(self, _name, _weapon, _hth, _atk, _def):
        super().__init__(_name,_hth,_atk,_def)
        self.weapon = _weapon

    '''
        REGION: ITEMS AND STATS
    '''
    #-///-:
    def itemAdd(self,itemName,itemDescription,itemRange):
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

    def itemUse(self, itemName):
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

    def itemApply(self,item):
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
        

    def itemPrint(self):
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

    '''
        BATTLE ACTION
    '''
    def battleAction(self, recipient):
        decision = input("where move next? "
                            + "\n1. attack"
                            + "\n2. defend"
                            + "\n3. useItem"
                            + "\n4. do nothing..."
		)

        if(decision == 1):
            self.attacking(currentWeapon.value)

        elif(decision == 2):
        
        elif(decision == 3):
        
        elif(decision == 4):

        else(decision)


        
        
    '''
    FIX FOR LATER

    public void battleAction(Monster recipient)
	{
		// prompt user for battle commands
		// add more commands like meditate or 
		System.out.println
		("where move next? "
				+ "\n1. attack"
				+ "\n2. defend"
				+ "\n3. useItem"
				+ "\n4. do nothing..."
		);

		// take users next input 
		int choice = input.nextInt();
		
		// stores how much damage the user did 
		int damageDealt = 0; 

		// cuts damage received in half when defending 
		if(recipient.defending == true)
		{
			// add an extra bit of defense to damage dealt
			damageDealt = ( (getAtk() - recipient.getDef()) / 2 );
			
			// turn of the "defending" state
			recipient.setdefend(false);
		}
		else 
		{
			// if they aren't defending make it normal damage
			damageDealt = (getAtk() - (recipient.getDef()));
		}

		// switch between users choice to find out what they want to do 
		switch(choice)
		{
			//1.up,  2.right, 3.down, 4.left, 5.show inventory, 6. useItem
			case 1:
				
				// attack monster // prints something like this (You attacked larry for 8 points of damage 
				System.out.println("You attacked " + recipient.getName() + " for " + damageDealt + " points of damage!" );
				recipient.setHealth(recipient.getHealth() - (damageDealt));
				break;

	
			case 2:
				// this just tells the enemy that the player is defending
				// this cause them to have extra defense from the next attack 
				System.out.println("You're defending from the next attack!");
				defending = true;
				break;
	
			case 3:
				// call useItem
				useItem();
				break;
				
			case 4:
				// do nothing 
				System.out.println("You did. nothing...");
				break;
			
			default:
				System.out.println("either incorrect or no input was entered therefore... SKIP A TURN!");
				break;
		}
	}
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
