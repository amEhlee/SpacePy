from Avatar import Avatar

class Player(Avatar):

    # initalize player variables
    inventory = {} # player inventory
    weapon = "" # might be a dicitonary later storing name : damage stuff

    #initalize constructor
    def __init__(self, _name, _weapon, _hth, _atk, _def):
        super().__init__(_name,_hth,_atk,_def)
        self.weapon = _weapon

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

