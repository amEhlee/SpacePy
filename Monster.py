

class Monster(Avatar):
    # initalize monster variables
    monster_health = 200  # store the monster's health
    monster_attack = [1, 3.5]  # store monster's attack in variable
    monster_aggro = 0  # manipulates monster's power (health) depending on choices made

    def __init__(self,health,attack,aggro):
        self.monster_health = health
        self.monster_attack = attack
        self.monster_aggro = aggro

    '''
    ATTACK VALUES REGION
    '''
    # return attack
    def getAttack(self):
        return self.monster_attack

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

    

