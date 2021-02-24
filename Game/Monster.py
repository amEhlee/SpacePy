from Avatar import Avatar

class Monster(Avatar):

	def __init__(self, mName, mHth, mAtk, mDef, mAggro):
		super().__init__(mName, mHth, mAtk, mDef)
		self.aggro = mAggro

	def battleAction(self, recipient):
		''' battle action specific to player monsters operate differently cause they can't choose actions'''
        decision = input("\nWhat action do you take?"
                            + "\n1. attack"
                            + "\n2. defend"
                            + "\n3. show inventory"
                            + "\n4. useItem"
                            + "\n5. do nothing..."
		)

        if(decision == "1"):
            #-///- possible expansion here for a second input tags as well as physical vs magic spells 
            # get damage
            damageDealt = self.calculateAttack(weaponValues)

            # factor defense cuts damage in two
            if(recipient.defending == True):
                print("The target was defending! Decreased Damage :(")
                damageDealt = self.calculateAttack(weaponValues)/2

                # reset defending 
                recipient.defending = False;

            # standard attacking 
            print("{} attacked {} for {} points of damage".format(self.name, recipient.name, damageDealt))
            recipient.health -= damageDealt

        elif(decision == "2"):
            print("You're Defending from the next attack")
            self.defending = True

        elif(decision == "3"):
            self.itemPrint()
        
        elif(decision == "3"):
            self.itemUse()
            
        elif(decision == "4"):
            print("You did. nothing...!")

        else:
            print("Invalid input.. retry!")
            self.battleAction(recipient)

    # toString method 
	def __str__(self):
        return("Hello my name is {}\nI have {} aggro so far \nHealth: {}\nAttack: {}\nDefense:{}\n\n".format(
            self.name,
            self.weapon,
            self.health,
            self.attack,
            self.defense
            ))

