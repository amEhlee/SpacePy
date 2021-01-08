from Avatar import Avatar

class Monster(Avatar):
    # initalize monster variables
    #aggro will be added later on 
    aggro = 0 

    def __init__(self,name,health,attack,defense,aggro):
        super(Avatar,self).__init__(name,health,attack,defense)
        self.aggro = aggro

    '''
    ATTACK VALUES REGION
    '''
    # set attack based on aggro
    def setAttack(self):
        # will use attack + aggro where if the monster has more aggro increase attack
        # aggro increases based on actions done to irritate the monster
        pass

    # increase aggro by a set amount
    def addAggro(self,amount):
        self.monster_aggro += amount

    '''
    EXTERNAL METHODS
    ''' 

    

