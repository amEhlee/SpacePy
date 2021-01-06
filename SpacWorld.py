class SpacWorld:

    import Monster
    import Player

    # import outside code to make stuff work with less complexity
    from random import uniform, randint
    from time import sleep  # anytime you see sleep(i) stops the program for i seconds
    import sys  # don't know too much about sys so I imported the whole thing / needed for print_slow

    # initalize miscellaneos
    text_read_speed = 0  # used for sleeping after text so I don't have to keep on setting it if I do change it
    effect = {}  # initalize text global effect variables

    # adds specific effects to the effect dictionary
    # links for effects http://ozzmaker.com/add-colour-to-text-in-python/
    effect['red'] = '\033[0;31m' 
    effect['green'] = '\033[0;32m'
    effect['yellow'] = '\033[0;33m'
    effect['blue'] = '\033[0;34m'
    effect['purple'] = '\033[0;35m'
    effect['cyan'] = '\033[0;36m'
    effect['blink1'] = '\033[5m'  # adds blink effect
    effect['blink2'] = '\033[6m' 

    '''
    all of these will be used for text writing later
    '''
    # this function makes it so text is printed to the screen slower than normal (like someone is typing)
    def print_slow(text, text_speed):
        for letter in text:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(text_speed)

    
    # This function adds effect to text
    def add_text_effect(effect_of_text, text):
        ending = '\033[0m'  # needs to be added to the end to reset things
        string_returned = ('{}' + text + '{}').format(effect_of_text, ending)
        return string_returned

    '''
    Choice options
    '''
    def showlayout(ship_state):
        '''originally has some drawn up ascii art that would be used for this
        and show where you were in the ship to better visualize ended up running out of time to implement this future
        and draw up more versions of the ship where it was destroyed and stuff.

        Maybe next time :c
        '''

class fullStory(SpacWorld):
    # start of the game 
    def start_Game(self):
        print("goto StorageRoom")

    # event 2: Storage room
    def start_StorageRoom(self):
        print("goto Hall_Way 1")

    # event 3: First Corridor
    def hallway_1(self):
        print("currently in hallway1")

class PlayGame(fullStory):
    fullStory.start_Game(1);

