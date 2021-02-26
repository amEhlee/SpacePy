from Avatar import Avatar 
import random

class Monster(Avatar):

    '''
        Initial Setup
    '''
    # Monster attribs @param aggro increases damamge @param species adds attributes to attacks like claws or sharp teeth 
    aggro = 0
    species = ""

    # monster species quotes
    SlimeQuotes = {
        1 : "Buy Low, Sell Slime?",
        2 : "You Think This Slime Is Just For Show?",
        3 : "Yadda Yadda Yadda"
    }

    def __init__(self, mName, mHth, mAtk, mDef, mAggro, mSpecies):
        super().__init__(mName, mHth, mAtk, mDef)
        self.aggro = mAggro
        self.species = mSpecies

    '''
        Battle Events
    '''

    def sayQuotes(self):
        if(self.species == "Slime"):
            quoteNum = random.randint(1,len(self.SlimeQuotes))
            print(self.SlimeQuotes[quoteNum])

    def battleAction(self, recipient):
        defending = False; # reset defending status 
        decision = random.randint(1,3); # use a random number to select action

        # pre calculate damage
        damageDealt = self.calculateAttack(self.mAtk)

        # factor defense cuts damage in two
        if(recipient.defending == True):
            print("The target was defending! Decreased Damage")
            damageDealt = damageDealt/2

            # reset defending 
            recipient.defending = False;


        if(decision == 1): # scratch
            # standard scratch attack
            print("{} attacked {} with a scratch for {} points of damage!".format(self.name, recipient.name, damageDealt))
            recipient.health -= damageDealt;

        elif(decision == 2): # bite
            # standard bite attack
            print("{} bit {} for {} points of damage!".format(self.name, recipient.name, damageDealt))
            recipient.health -= damageDealt;

        elif(decision == 3): # defend 
            print("{} is now defending!".format(self.name))
            defending = True;