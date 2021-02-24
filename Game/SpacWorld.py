from Player import Player
from Monster import Monster
from Item import Item
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

    # List of Common Items used to easily identify consumables and items used more than once
    # -///- : actually add items here lol
    iGreen_Syringe = Item("potion","heal for x hp",[0.1,0.5],1,"Consumable")
    iWeaponWrench = Item("Wrench","deals 0.1 - 0.5 extra damage",[0.1,0.5],None,"Weapon")
    iWeaponDefault = Item("Hands","Deals a small amount of damage",[0.1,0.5],None,"Weapon")
    iArmorDefault = Item("SkinSuit","Bare suit made for a slight more confortable time in space",[0.3,0.5],None,"Armor")
    iArmorSuit = Item("SpaceSuit","Bulky and More importantly made to protect",[0.5,0.8],None,"Armor")

    # initalize miscellaneos
    text_read_speed = 0  # used for sleeping after text so I don't have to keep on setting it if I do change it
    text_slow_speed = 0 # used for the print slow method 
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
    Character Creation o is prefixed for object
    '''
    oPlayer = Player(None,None,None,None,None)
    oMonster = Monster("Monster",200,20,20,0)

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
            , self.text_slow_speed)
        print('\n')
        self.sleep(self.text_read_speed)
        self.characterCreation()

    # Character Creation
    def characterCreation(self):
        # Process player decisions on Name 
        decision = input(self.add_text_effect(self.effect['yellow'],
                            "What is the name of your character"))

        # Apply player name decision
        self.oPlayer.name = decision

        # Process player decisions on Play style
        decision = input(self.add_text_effect(self.effect['yellow'],
                    "\nWhat style of play of you have? (Choose a number!!)\n1: Offensive 100 health 25 attack 10 defense\n2: Defensive 150 Health, 15 attack 20 defense\n3. Neutral 125 Health 15 attack, 15 defense"))
        
        # Apply player stats decision
        if(decision == '1'):
            self.oPlayer.health = 100
            self.oPlayer.attack = 25
            self.oPlayer.defense = 10
        elif(decision == '2'):
            self.oPlayer.health = 150
            self.oPlayer.attack = 15
            self.oPlayer.defense = 25
        elif(decision == '3'):
            self.oPlayer.health = 125
            self.oPlayer.attack = 15
            self.oPlayer.defense = 15
        else:
            print("invalid input, retrying method...")
            self.characterCreation()

        # More responeses
        self.print_slow("Perfect!\nBe aware that weapons and Armor can also be found within the game that will help you", self.text_slow_speed)
        self.print_slow("Here are your Player's total stats right now", self.text_slow_speed )
        self.oPlayer.__str__()
        self.print_slow("\n\nHave fun and hope you enjoy the game\n\n\n", self.text_slow_speed)
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
            if (self.randint(0, 100) < 50):
                # print text
                print(self.add_text_effect(self.effect["green"],
                                    "In one of the cardboard boxes you find a syringe filled with a green liquid! This could can probably be used to heal you later on"))
                
                # add stuff to inventory and show what you already have
                self.oPlayer.itemAdd(self.iGreen_Syringe)
                self.oPlayer.itemPrint()
                
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
            self.oMonster.aggro += 20 

        elif(repeat_count >= 4):
            # nothing is left in the room so continue printing this
            print("The only thing that remains is silence")

        # first decision asks to leave room or wait/search
        decision = input(self.add_text_effect(self.effect['cyan'],
            "\nThings seem pretty quiet outside should I leave the room? \n 1. Leave the room \n 2. Search the room in silence for anything useful"))
        
        if (decision == "1"):
            # move on to the next part of the game
            repeat_count = 0  # checks how many times the function repeats
            self.hallway_1()

        else:
            # run this function again but not with the same text
            print('\n')
            repeat_count += 1  # checks how many times the function repeats
            self.storage_room(repeat_count)


    def hallway_1(self):
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
        decision = input(self.add_text_effect(self.effect['cyan'],
            "\nDo you go over and investigate the suit? \n1. Yes maybe you could find out more about that sludge \n2. Not with all the green sludge covering it!"))

        if (decision == '1'):
            # if they choose to check the suit move to that function
            self.investigate_suit()

        elif (decision == '2'):
            # if they don't move along
            self.fork_1()

    def investigate_suit(self):
        # print a bunch more plot with waits inbetween
        print('\n')
        print("You turn over and investigate the space suit making sure to avoid the gel")
        self.sleep(self.text_read_speed)
        print(
            "Past the helmet you can see the suit itself is filled to the brim with that same green slime that seems to have consumed whatever used to be inside")
        self.sleep(self.text_read_speed)
        # print what happened with a red color so you know you got hurt
        print(self.add_text_effect(self.effect['red'],
            "as you try to take a closer the green goo bursts out of the helmet slightly burning your hand. From this you take 10 damage"))
        # decrease player health cause they made the wrong decision
        self.oPlayer.health -= 10
        print(("You now have {} points of health").format(self.oPlayer.health))
        # move along to the next part of the story a fork in the path
        self.fork_1()

    def fork_1(self):
        # next part in story fork in the path
        # print lots of text with more sleeps
        print(
            "\n Ahead of you now stands two paths: The first heads directly to the research sector and the second follows a hallway around it")
        self.sleep(self.text_read_speed)
        print(
            "Though you it might be a good idea to explore the research area for anything useful taking the hallway around it might be faster and much less dangerous")
        self.sleep(self.text_read_speed)

        # make the user decide on what path to take
        decision = input(self.add_text_effect(self.effect['cyan'],
            "\What path do you want to take? \n1. To the research sector! \n2. The research sector is too dangerous seems like a better idea to go around it "))

        if (decision == "1"):
            # move to research sector
            self.research_sector()

        elif (decision == "2"):
            # alternative to research sector
            self.hallway_2()


    def hallway_2(self):
        # this is the hallway alternative to the research_sector
        # print text with waits
        print('\n')
        print(
            "This hallway seems empty of life but has an eccesive amount of green gel hanging from the walls and ceiling vents")
        self.sleep(self.text_read_speed)
        # print text in red to show user did something wrong and took damage
        print(self.add_text_effect(self.effect['red'],
                            "As you make your way through the hallway from above you the ceiling collapses from goo weighing it down dealing 20 points of damage"))
        self.sleep(self.text_read_speed)
        # decrease and print the player's current health
        self.oPlayer.health -= 20
        print(("You now have {} points of health").format(self.oPlayer.health))
        # move to next part of the game
        self.fork_2()


    def research_sector(self):
        # this is the research sector part of the game
        # print text with waits inbetween
        print('\n')
        print(
            "The research sector is full of the obvious, various shapes and sizes of vials, bunsen burners, microscopes and bottles of God knows what. As well as the green gel which drips from the ceiling vents every few seconds")
        self.sleep(self.text_read_speed)
        print("While searching the room you spot some gel land in a empty vial above a live bunsen burner.")
        self.sleep(self.text_read_speed)

        # show text in yellow to show that it is of value
        # lets the player know the alien is weak to heat (hopefully)
        print(self.add_text_effect(self.effect['yellow'],
                            "the heat from the flame causes the gel to come to a boil and evaporate. In response to this the surronding gel goes lifeless"))
        self.sleep(self.text_read_speed)

        # decide whether to pick up the heat ray or not
        decision = input(self.add_text_effect(self.effect['cyan'],
                            "On top of a nearby desk you spot a heat ray \n1. Pick it up \n2. leave it alone might be dangerous \n"))

        if (decision == '1'):
            # print text of trying heat ray with waits inbetween
            # this might want to be expanded on -///-
            print('\nYou pick up and try to use the heat ray but it seems to be either broken or out of juice')
            self.sleep(self.text_read_speed)
            print('You leave it alone and move on')
            # move on to next part of game
            self.fork_2()

        elif (decision == '2'):
            # print text and move on
            print('You leave it alone and move on')
            self.fork_2()


    def fork_2(self):
        # asks if the user want to go to either to medbay or alternative hallway
        print(
            "There is another fork in the road either go to the medbay which oozes with green gel from under the door or the alternative path around it which might be safer as well as faster ")
        self.sleep(self.text_read_speed)

        # lets the player decide where to go next
        decision = input(self.add_text_effect(self.effect['cyan'],
                             "\n1. Go to medbay \n2. Take the hallway around which might be safer"))

        if (decision == '1'):
            # goes down medbay route
            self.medbay()

        elif (decision == '2'):
            # goes down alternative to medbay route
            self.hallway_3()


    def medbay(self):
        # print text for medbay route with wait's inbetween print statemnents
        print('\n')
        print("The medbay looks like any old regular hospital. White beds and first aid kits line the room")
        self.sleep(self.text_read_speed)
        print(
            'In the room there are also a number of spacesuits on the ground, beds, everywhere! They are all filled with gel which based on instinct you stay away from')
        self.sleep(self.text_read_speed)
        # let the user know they picked up a healing syringe in green text green = good
        print(
            self.add_text_effect(self.effect['green'], 'Lying on a matress you see a green health syringe which you take for later'))
        
        # add to inventory 
        self.oPlayer.itemAdd(self.iGreen_Syringe)
        self.sleep(self.text_read_speed)

        # lets the user know what they have in their inventory
        self.oPlayer.itemPrint()
        self.sleep(self.text_read_speed)

        # go to next part of the game(cockpit)
        self.cockpit()


    def hallway_3(self):
        # alternative route from fork in road
        # print text and go to next part of the game(cockpit)
        print("\nThe hallway is filled with nothing but silence. You can tell the green jelly has taken over some bathrooms nearby so no getting near that.")
        self.sleep(self.text_read_speed)
        self.cockpit()


    def cockpit(self):
        # part of the game where the player is in the cockpit/control room of the ship
        # print more plot with waits inbetween
        print('\nYou enter the cockpit of the ship. On its walls are monitors of various sizes')
        self.sleep(self.text_read_speed)
        print('You turn on the main screen and enter the password to open the ship docking sector')
        self.sleep(self.text_read_speed)
        print("words flash on the screen saying" + self.add_text_effect(self.effect['yellow']," SHIP DOCKING SECTOR NOW OPEN."))
        #print("words flash on the screen saying" + "\033[0;33m \033[5m SHIP DOCKING SECTOR NOW OPEN.\033[0m")
        self.sleep(self.text_read_speed)
        print(
            'You turn off the screen and search the room. On a nearby table you find a large wrench which might serve as a good weapon \n')
        self.sleep(self.text_read_speed)
        # decision to pick up the wrench or not
        decision = input(self.add_text_effect(self.effect['cyan'],
                            "Do you pick up the wrench \n1. Pick up the wrench \n2. leave it alone"))

        if (decision == '1'):
            # if the player chooses to pick up the wrench add it as their main weapon
            # this weapon will be used for combat later on
            print("\nYou now have the wrench as your main weapon")
            self.sleep(self.text_read_speed)
            self.oPlayer.itemAdd(self.iWeaponWrench)
            #weapon = wrench -///- possible problem area 
            # continue the scene in the cockpit
            self.cockpit_continued()

        elif (decision == '2'):
            # continue the scene in the cockpit if they don't pick it up
            self.cockpit_continued()


    def cockpit_continued(self):
        # print more text with waits inbetween
        print(
            'You also spot below the large monitor a large red button trapped in a glass case with text on it saying "SELF DESTRUCT"')
        self.sleep(self.text_read_speed)
        print("It might be able to take out the alien on this ship no gurantee that it won't take you along too though")
        self.sleep(self.text_read_speed)
        # decide whether or not to press the button that activates self destruct sequence
        decision = input(self.add_text_effect(self.effect['red'],
                        "\nDo you press the button? \n1. Activate self destruct button \n2. Leave it alone and move on"))

        if (decision == '1'):
            # moves to self destruct sequence part of game
            self.self_destruct()

        elif (decision == '2'):
            # moves to next part of the game
            self.explosion()


    def self_destruct(self):
        # moves to self destruct sequence part of the game
        print('\n')
        # increases monster aggro cause you chose the right option effectively activating hardmode
        self.oMonster.aggro += 100
        # self_destruct? = true; this changes ending of the game and acftivates other things like hardmode SHOULD TRIGGER MORE EVENTS

        # print flashing red text for effect
        print(
            'As you pound the bottom down every screen lights up with the words' + '\033[1m \033[0;31m \033[6m WARNING!  WARNING! SELF DESTRUCT SEQUENCE ACTIVATED! WARNING!  WARNING!\033[0m')
        self.sleep(self.text_read_speed)
        print('followed by a timer that starts counting down:')
        self.sleep(self.text_read_speed)

        # for loop that prints a timer
        timer_countdown = ['3:00', '2:59', '2:58', '...']

        for numbers in timer_countdown:
            print(numbers)
            self.sleep(1)


        # moves to next part of the game
        self.explosion()


    def explosion(self):
        # print more plot with waits inbetween
        print('\n')
        print('As you rush your way out the room you hear a loud explosion and the ship begins to sway back and forth')
        self.sleep(self.text_read_speed)
        print('You also see more of the green slime collapse into the room and begin to chase you')
        self.sleep(self.text_read_speed)
        print(
            'You sprint past the past the medbay, research sector and hallways as waves of sludge covers the path behind you')
        self.sleep(self.text_read_speed)
        print("You finally arrive back where you started and bolt through the now open ship dock steel doors")
        self.sleep(self.text_read_speed)
        print(
            'As you attempt to make it to the nearest escape ship the mass of slime swerves around you and blocks your path')
        self.sleep(self.text_read_speed)
        print('The lime slime forms a mass of jelly infront of you with one eye that stares in your direction')
        self.sleep(self.text_read_speed)

        # adds the monster's aggro (how much it hates you ) to its health based on old decisions
        # monster aggro should be processed in a different way self.oMonster.health += monster_aggro
        # -///-
        self.oMonster.health += self.oMonster.aggro

        # Enter combat with the slime
        print("You now enter combat with the slime alien! \n")
        self.battleScript(self.oMonster)

    '''
    MAIN HEADER BUT BATTLES SHOULD BE CLEANED UP A LOT MORE THAN THIS 
    '''
    def battleScript(self, recipient):
        while((self.oPlayer.health > 0) and (recipient.health > 0)):
            #print a break including player and monster information
            print("\n\n---- BATTLE ---- \n\n")
            print("{} has {} health points remaining".format(recipient.name, recipient.health));
            print("{} has {} health points remaining".format(self.oPlayer.name,self.oPlayer.health))

            # monster taunts player
            #recipient.sayQuote() -///-

            # allow player to attack
            self.oPlayer.battleAction(recipient)

            # make recipient attack back 
            recipient.battleAction(oPlayer)

        # battle over. go home.
        self.ending();


    def ending(self):
        # decides what ending the player got
        if (self.oMonster.health <= 0):
            # if the monster died move on
            print("\n")

            if (self.oMonster.aggro >= 100):
                # checks based on monster's aggro cause that increses by 100 when you press the switch
                # if the monster died AND you activated the self destruct sequence go to the best ending
                win_situation_good()

            else:
                # if they didn't press the switch BUT defeated the monster go to the neutral ending
                win_sitation_neutral()

        elif (self.oPlayer.health <= 0):
            # if they lost the battle print this sitation
            lose_sitation()


    def win_situation_good(self):
        # print the best ending to the game and exit from the game
        print(('\n') * 3)
        print(self.add_text_effect(self.effect['blue'],
                            "After you defeat the slime you quickly enter a nearby space craft and blast off while loud explosions resound behind you"))
        self.sleep(self.text_read_speed)
        print(self.add_text_effect(self.effect['blue'], "The explosion destroys the Atlas and no life signs remain "))
        self.sleep(self.text_read_speed)
        # print the text letter by letter
        print_slow(self.add_text_effect(self.effect['blue'], "You got the best ending the galaxy is saved", 0.1))
        exit()


    def win_sitation_neutral(self):
        # print the neutral ending's text and exit from the game
        print(('\n') * 3)
        print(self.add_text_effect(self.effect['blue'],
                            "After you defeat the slime you quickly enter a nearby spaceship and blast off of the EKS Atlas"))
        self.sleep(self.text_read_speed)
        print(self.add_text_effect(self.effect['blue'],
                            "You win! You managed to escape from the spaceship with your life though as the ship disappears from your view you can't help but feel unsettled."))
        self.sleep(self.text_read_speed)

        # print the text letter by letter
        print_slow(
            "Years later you hear news that the planet jupitaa had been taken over by some strange slime but it doesn't seem like its stopping there....",
            0.1)
        print_slow("YOU GOT THE NEUTRAL ENDING", 0.1)
        exit()


    def lose_sitation(self):
        # print the loss ending's text and exit from the game
        print(('\n') * 3)
        print(self.add_text_effect(self.effect['blue'],
                            "The slime quickly dispatches you like it did to the rest of the crew. You feel moisture seep into your spacesuit and you pass out shortly after"))
        self.sleep(self.text_read_speed)
        print(self.add_text_effect(self.effect['blue'], "You lose. The galaxy has been taken over by slime and no life signs remain"))
        # print the text letter by letter
        print_slow("YOU GOT THE WORST ENDING", 0.1)
        exit()
