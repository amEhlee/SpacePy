import math
import random

class Avatar:

    # attributes that every character should have
    name = None;
    heath = None;
    magic = None;

    # base constructor for object creation
    def __init__(self, _name,_health,_magic):
        self.name = _name
        self.health = _health
        self.magic = _magic 

    def getName(self):
        return self.name

    def setName(self, _name):
        self.name = _name

    '''
    HEALTH REGION
    '''
    def getHealth(self):
        return self.monster_health
    
    def setHealth(self,health):
        self.monster_health = health


    # this function takes two args (min and max) and returns a random number between them
    # this should take pretty low numbers so enemies arent broken
    def attacking(self,attack_value):
        min_value = attack_value[0]
        max_value = attack_value[1]
        crit = False  # initalize crit chance varible
        attack = math.uniform(min_value, max_value)  # returns a random number between min and max

        if random.randint(0, 100) < 10:
            # 10% chance for a critical attack to occur
            crit = True

        if (crit == True):
            # if crit chance is true multiple attack by 20
            attack = round(attack, 1) * 20
        else:
            # else multiply by 10 for regular attack
            attack = round(attack, 1) * 10
            # return attack
            print('This action has %s points' % attack)
        return attack

    

    def toString(self):
        return "my name is {},\nHealth: {}\nMagic: {}".format(self.name,
                                                                self.health,
                                                                self.magic
                                                                )

