from Avatar import Avatar

class Monster(Avatar):
    # initalize monster variables
    #aggro will be added later on 
    aggro = 0 

    def __init__(self,name,health,attack,defense,aggro):
        super().__init__(name,health,attack,defense)
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

    def __str__(self):
        return "my name is {},\nHealth: {}\nAttack: {}\nDefense: {}\n".format
            (
                
                self.name,
                self.health,
                self.attack,
                self.defense
            )




    class Parent():
        myvar = 0
        x = 0
        y = 0

        def __init__(self):
            self.x = 1 
            self.y = 12 

    class Child(Parent):
        def __init__(self):
            super().__init__()

            # here you can access myvar like below.
            print(self.myvar,self.x,self.y)

    child = Child()
    print(child.myvar)