from Avatar import Avatar

class Monster(Avatar):
    # base monster variables
    aggro = 0 

    def __init__(self,mName,mHth,mAtk,mDef,mAggro):
        super().__init__(mName,mHth,mAtk,mDef)
        self.aggro = mAggro

    '''
    MUTATORS
    '''
    #def addAggro # will play throughout dungeon
    #def playRound #monster attack phasew


    '''
    EXTERNAL METHODS
    ''' 

    def __str__(self):
        return("Hello my name is {}\nI have {} aggro so far\nHealth: {}\nAttack: {}\nDefense:{}\n\n".format(
                self.name,
                self.aggro,
                self.health,
                self.attack,
                self.defense
            ))
