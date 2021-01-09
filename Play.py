from Player import Player
from Monster import Monster

class play:
    
    p = Player("Larry","Branch",100,10,5)
    m = Monster("Monster",200,20,30,10)

    print(p.__str__())
    print(m.__str__())