from Player import Player
from Monster import Monster
from time import sleep
import sys

'''
    holds the main story of the game and all key decision events
    all of this will be run later in the main method via startGame
'''
class SpacWorld:

    # default constructor
    def __init__(self):
        # start the game at the creation of a new instance
        self.start_game()

    # import outside code to make stuff work with less complexity
    from random import uniform, randint
    from time import sleep  # anytime you see sleep(i) stops the program for i seconds
    import sys  # don't know too much about sys so I imported the whole thing / needed for print_slow

    # initalize miscellaneos
    text_read_speed = 1  # used for sleeping after text so I don't have to keep on setting it if I do change it
    repeat_count = 0 # checks how many times a fuction repeats // used multiple times
    effect = {}  # initalize text global effect variables

    # adds specific effects to the text effect dictionary
    # links for effects http://ozzmaker.com/add-colour-to-text-in-python/
    effect['red'] = '\033[0;31m' 
    effect['green'] = '\033[0;32m' 
    effect['yellow'] = '\033[0;33m'
    effect['blue'] = '\033[0;34m'
    effect['purple'] = '\033[0;35m'
    effect['cyan'] = '\033[0;36m'
    effect['blink1'] = '\033[5m'  # adds blink effect
    effect['blink2'] = '\033[6m'  # faster blink event

    '''
    TEXT AND FORMATTING
    '''
    # this function makes it so text is printed to the screen slower than normal (like someone is typing)
    def print_slow(self,text, text_speed):
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(text_speed)

    
    # This function adds effect to text
    def add_text_effect(self,effect_of_text, text):
        ending = '\033[0m'  # needs to be added to the end to reset things
        string_returned = ('{}' + text + '{}').format(effect_of_text, ending)
        return string_returned

    '''
    Choice options
    '''
    def showlayout(self,ship_state):
        '''originally has some drawn up ascii art that would be used for this
        and show where you were in the ship to better visualize ended up running out of time to implement this future
        and draw up more versions of the ship where it was destroyed and stuff.

        Maybe next time :c
        '''

    '''
    Character Creation
    a = ally
    e = enemy
    '''
    aPlayer = Player(None,None,None,None,None)
    eMonster = Monster("Monster",200,20,20,0)

    '''
    Story Options
    '''
    # starts the game
    def start_game(self):
        print('\n')
        # prints the introduction to the game and lets the user know whats going on
        self.print_slow(
            '''You are a member of the EKS Atlas. A research vessel headed for the planet Jupitaa. When your ship was breeched by some strange alien force. 
            Your goal is now to find a way out of the ship while avoiding whatever creature got to rest'''
            , 0.1)
        print('\n')
        self.sleep(self.text_read_speed)
        self.characterCreation()

    # Character Creation
    def characterCreation(self):

        # Process player decisions on Name 
        decision = input("what is the name of your character")

        # Apply player name decision
        self.aPlayer.name = decision

        # Process player decisions on Play style
        decision = input("what style of play of you have? (Choose a number!!)\n1: Offensive 100 health 25 attack 10 defense\n2: Defensive 150 Health, 15 attack 20 defense\n3. Neutral 125 Health 15 attack, 15 defense")

        # Apply player stats decision
        if(decision == '1'):
            self.aPlayer.health = 100
            self.aPlayer.attack = 25
            self.aPlayer.defense = 10
        elif(decision == '2'):
            self.aPlayer.health = 150
            self.aPlayer.attack = 15
            self.aPlayer.defense = 25
        elif(decision == '3'):
            self.aPlayer.health = 125
            self.aPlayer.attack = 15
            self.aPlayer.defense = 15
        else:
            print("invalid input, retrying method...")
            self.characterCreation()

        # More responeses
        self.print_slow("Perfect!\nBe aware that weapons and Armor can also be found within the game that will help you",0.1)
        self.print_slow("Here are your Player's total stats right now",0.1)
        self.aPlayer.__str__()
        self.print_slow("Have fun and hope you enjoy the game",0.1)
        self.sleep(self.text_read_speed)

        # moves the story to the storage room function
        self.storage_room(self.repeat_count)  

    # Hiding in the storage room
    def storage_room(self,repeat_count):
        if(repeat_count == 0):
            # if this is your first time do all this stuff
            print(
                "You awake in what looks to be a storage room. Its cramped, cold and filled to the brim with boxes containing equipment, food, water and the like")
            self.sleep(self.text_read_speed)
            print(
                "You get up out of the mixture of cardboard and hard plastic and onto your feet. Your head hurts and you feel a consistent sense of dread. Other then your breathing things seem to be oddly quiet")
            self.sleep(self.text_read_speed)

        elif(repeat_count == 1):
            # if this is your second time print all this stuff
            # random chance to find healing syringe in this room that can be used in battles
            if (randint(0, 100) < 50):
                # print text
                print(add_text_effect(effect["green"],
                                    "In one of the cardboard boxes you find a syringe filled with a green liquid! This could can probably be used to heal you later on"))
                
                # add stuff to inventory and show what you already have
                self.aPlayer.inventory.append("Green Syringe")
                print(("in your inventory you got:" + '{}').format(inventory))
                
                # print text
                print("Things outside haven't changed")

            else:
                # if lady luck didn't bless you print this
                print(
                    "In the mass of cardboard and scraps you find nothing of use. Outside of the storage room things are still oddly quiet")

        elif(repeat_count == 2):
            # if this is your third time print this
            print("nothing seems to of changed outside... or in the room. Maybe its time to go..?")

        elif(repeat_count == 3):
            # if this is your forth time print this
            print(
                "Suddenly a thundering crash like a glass dish falling breaks the silence outside the door, followed by a single pair of foot steps that get quieter as something rushes away")
            print("the silence resumes... For some reason you feel just a little bit safer")

            # Waited long enough so monster no longer suspects you. reduce aggro by 20
            eMonster.aggro += 20 

        elif(repeat_count >= 4):
            # nothing is left in the room so continue printing this
            print("The only thing that remains is silence")

        # first decision asks to leave room or wait/search
        decision = input("\n \033[0;36mThings seem pretty quiet outside should I leave the room? \n 1. Leave the room \n 2. Search the room in silence for anything useful \033[0m")
        if (decision == "1"):
            # move on to the next part of the game
            repeat_count = 0  # checks how many times the function repeats
            hallway_1()

        else:
            # run this function again but not with the same text
            print('\n')
            repeat_count += 1  # checks how many times the function repeats
            storage_room()


    def hallway_1():
        print('\n')
        # print a bunch of text with pauses in between
        print(
            "You exit the room and enter the large and now luminicent hallway. Though things seem different from what you remember...")
        self.sleep(self.text_read_speed)
        print(
            "The lights are off and The hallway is devoid of any crew members. The walls have been caked in a strange unfamillar green gel which seem to be the source of the corridor's lime glow")
        self.sleep(self.text_read_speed)
        print(
            "The ship docking area the only resonable exit off the ship is south of where you are. Though heavy steel doors block the passage.")
        self.sleep(self.text_read_speed)
        print(
            "In order to get them back open you'll need to head to the front of the ship and release the backup power holding the doors shut")
        self.sleep(self.text_read_speed)
        print(
            "\nUnable to go to south you go north towards the research area and medbay when you spot a lone spacesuit lying facedown on the ground. ")
        self.sleep(self.text_read_speed)
        print("Its covered in that strange green goop and brings an aura of curiosity as well as fear")

        # decide whether to go and investigate the suit or move along
        decision = input(
            "\n \033[0;36mDo you go over and investigate the suit? \n1. Yes maybe you could find out more about that sludge \n2. Not with all the green sludge covering it! \033[0m")
        if (decision == '1'):
            # if they choose to check the suit move to that function
            investigate_suit()

        elif (decision == '2'):
            # if they don't move along
            fork_1()

    def investigate_suit(self):
        # print a bunch more plot with waits inbetween
        print('\n')
        print("You turn over and investigate the space suit making sure to avoid the gel")
        self.sleep(self.text_read_speed)
        print(
            "Past the helmet you can see the suit itself is filled to the brim with that same green slime that seems to have consumed whatever used to be inside")
        self.sleep(self.text_read_speed)
        # print what happened with a red color so you know you got hurt
        print(add_text_effect(effect['red'],
                            "as you try to take a closer the green goo bursts out of the helmet slightly burning your hand. From this you take 10 damage"))
        # decrease player health cause they made the wrong decision
        self.aPlayer.health -= 10
        print(("You now have {} points of health").format(self.aPlayer.health))
        # move along to the next part of the story a fork in the path
        fork_1()

    def fork_1(self):
        print("end for now :Printing Player Stats")
