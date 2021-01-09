from Player import Player
from Monster import Monster

'''
    holds the main story of the game and all key decision events
    all of this will be run later in the main method via startGame
'''
class SpacWorld:
    # import outside code to make stuff work with less complexity
    from random import uniform, randint
    from time import sleep  # anytime you see sleep(i) stops the program for i seconds
    import sys  # don't know too much about sys so I imported the whole thing / needed for print_slow

    # initalize miscellaneos
    text_read_speed = 1  # used for sleeping after text so I don't have to keep on setting it if I do change it
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
    //////////////////////// prompt player name here //////////////
    aPlayer = Player()
    eMonster = Monster("Monster",200,20,20,0)

    '''
    Story Options
    '''
    # starts the game
    def start_game():
        print('\n')
        # prints the introduction to the game and lets the user know whats going on
        print_slow(
            '''You are a member of the EKS Atlas. A research vessel headed for the planet Jupitaa. When your ship was breeched by some strange alien force. 
            Your goal is now to find a way out of the ship while avoiding whatever creature got to rest'''
            , 0.1)
        print('\n')
        sleep(text_read_speed)
        storage_room()  # moves the story to the storage room function

    # Hiding in the storage room
    def storage_room():
        repeat_count  # checks how many times the function repeats
        if (repeat_count == 0):
            # if this is your first time do all this stuff
            print(
                "You awake in what looks to be a storage room. Its cramped, cold and filled to the brim with boxes containing equipment, food, water and the like")
            sleep(text_read_speed)
            print(
                "You get up out of the mixture of cardboard and hard plastic and onto your feet. Your head hurts and you feel a consistent sense of dread. Other then your breathing things seem to be oddly quiet")
            sleep(text_read_speed)

        elif (repeat_count == 1):
            # if this is your second time print all this stuff
            # random chance to find healing syringe in this room that can be used in battles
            if (randint(0, 100) < 50):
                # print text
                print(add_text_effect(effect["green"],
                                    "In one of the cardboard boxes you find a syringe filled with a green liquid! This could can probably be used to heal you later on"))
                # add stuff to inventory and show what you already have
                inventory.append("Green Syringe")
                print(("in your inventory you got:" + '{}').format(inventory))
                # print text
                print("Things outside haven't changed")

            else:
                # if lady luck didn't bless you print this
                print(
                    "In the mass of cardboard and scraps you find nothing of use. Outside of the storage room things are still oddly quiet")

        elif (repeat_count == 2):
            # if this is your third time print this
            print("nothing seems to of changed outside... or in the room. Maybe its time to go..?")

        elif (repeat_count == 3):
            # if this is your forth time print this
            print(
                "Suddenly a thundering crash like a glass dish falling breaks the silence outside the door, followed by a single pair of foot steps that get quieter as something rushes away")
            print("the silence resumes and you feel somewhat safer")
            # since you waited long enough the monster goes away and is no longer suspicious
            global monster_aggro
            monster_aggro -= 50  # this will decrease monster health later cause it no longer suspects you

        elif (repeat_count >= 4):
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
        sleep(text_read_speed)
        print(
            "The lights are off and The hallway is devoid of any crew members. The walls have been caked in a strange unfamillar green gel which seem to be the source of the corridor's lime glow")
        sleep(text_read_speed)
        print(
            "The ship docking area the only resonable exit off the ship is south of where you are. Though heavy steel doors block the passage.")
        sleep(text_read_speed)
        print(
            "In order to get them back open you'll need to head to the front of the ship and release the backup power holding the doors shut")
        sleep(text_read_speed)
        print(
            "\nUnable to go to south you go north towards the research area and medbay when you spot a lone spacesuit lying facedown on the ground. ")
        sleep(text_read_speed)
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

    def investigate_suit():
        # print a bunch more plot with waits inbetween
        print('\n')
        print("You turn over and investigate the space suit making sure to avoid the gel")
        sleep(text_read_speed)
        print(
            "Past the helmet you can see the suit itself is filled to the brim with that same green slime that seems to have consumed whatever used to be inside")
        sleep(text_read_speed)
        # print what happened with a red color so you know you got hurt
        print(add_text_effect(effect['red'],
                            "as you try to take a closer the green goo bursts out of the helmet slightly burning your hand. From this you take 10 damage"))
        # decrease player health cause they made the wrong decision
        player.health -= 10
        print(("You now have {} points of health").format(player_health))
        # move along to the next part of the story a fork in the path
        fork_1()

    def fork_1():
        print("end for now :Printing Player Stats")


    

