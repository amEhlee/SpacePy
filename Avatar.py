import math
import random

class Avatar():

    # attributes that every character should have
    name = None
    health = None
    attack = None 
    defense = None

    # base constructor for object creation
    def __init__(self, _name, _health, _attack, _defense):
        self.name = _name
        self.health = _health
        self.attack = _attack
        self.defense = _defense

    # this function takes two args (min and max) and returns a random number between them
    # this should take pretty low numbers so enemies arent broken
    def attacking(self,attack_value):
        min_value = attack_value[0]
        max_value = attack_value[1]
        crit = False  # initalize crit chance varible
        attack = math.uniform(min_value, max_value)  # returns a random number between min and max

        # Possible crit chance on every hit using randint
        if random.randint(0, 100) < 10:
            # 10% chance for a critical attack to occur
            print("CRITICAL HIT")
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

    # Process all damage taken to self and use attacking method from before 
    def takeDamage(self,points):
        self.health -= attacking(points)

    # toString method returns values of all attribs
    def __str__(self):
        return "my name is {},\nHealth: {}\nAttack: {}\nDefense: {}\n".format
        (
            self.name,
            self.health,
            self.attack,
            self.defense
        )

