import sys
import os
import random

#the expected arguments for each creature entry in a config file
EXPECTED_ARGS = ["NAME", "TOKEN", "INITIATIVE", "ATTACKS", "MOVEMENT", "HP",
                 "AC"]

#commands to be used in the main menu, this is just the help really though.
#the actual definition of what these commands do is implemented in the main
#menu itself
COMMANDS = {"load <file1> [file2] [file3] ...":
                "Loads files into combat buffer",
            "list":
                "List all of the files that are to be loaded for combat",
            "remove <file>":
                "Remove file from combat buffer",
            "start":
                "start combat with files in buffer",

            "bash <command>":
                "quickly run a single bash command",
            "math <expression>":
                "quickly evaluate a math expression",

            "exit":
                "get out of this menu and exit program"
        }

#commands for the main combat menu
COMBAT_COMMANDS = {
            "help": "show this help",
            "show|list": "shows the health of all creatures in combat",
            "damage <creature> <ammount>":
                "listed takes or gain the ammount of health listed",
            "heal <creature> <ammount>":
                "heals given greature by given ammount",
            "purge": "drops all creatures with health below 0 from the list",
            'who|turn': "shows who's turn it currently is",
            "attack": "enters the attacking menu for the current creature",
            "kill": "remove a creature from the list of creatures in combat"
        }


def roll_for_initiative(creatures):
    """
        Rolls a d20 and adds it to the initiative modifier
    """
    for creature in creatures:
        creature['INITIATIVE'] = creature['INITIATIVE'] + random.randint(1, 20)
    return creatures

def sort_by_initiative(creatures):
    """
        takes in a list of dicts representing all of the creatures in combat,
        returns a new list of dicts that is the same creatures but sorted by
        initiative
    """
    s_creatures = []
    while creatures:
        l_index = l_value = 0
        for ii, creature in enumerate(creatures):
            if creature['INITIATIVE'] > l_value:
                l_value = creature['INITIATIVE']
                l_index = ii

        s_creatures.append(creatures.pop(l_index))
    return s_creatures

def die(*args):
    """
        print args and then exit
    """
    for each in args:
        print(each)
    print("exiting..")
    exit()


def verify_expected_args(creature):
    global EXPECTED_ARGS
    for arg in EXPECTED_ARGS:
        if arg not in creature.keys():
            die("Was not able to find arg {} in creature def".format(arg))

def parse_arg(arg, value):
    if arg == 'ATTACKS':
        attacks = []
        weapons = value.split(';')
        for _weapon in weapons:
            weapon = {}
            found_name = False
            for entry in _weapon.split(','):
                if ':' not in entry:
                    if found_name: die("Found multiple names for weapon!")
                    weapon['name'] = entry
                    found_name = True
                    continue
                split = entry.split(':')
                weapon[split[0]] = split[1]
            attacks.append(weapon)
        return attacks

    elif arg in ['INITIATIVE', "MOVEMENT", 'HP', 'AC']:
        return int(value)

    else:
        return value

def parse_config_file(filename):
    """
        Opens up a combat config file and parses all of the entries into dicts
    """
    creatures = []
    creating_creature = False
    with open(filename) as f:
        current_creature = {}
        for line in [_line.strip() for _line in f]:
            if not line or len(line) == 0:
                continue

            if line[0] == '@':
                split = line[1:].split()
                if split[0] == 'NEW':
                    if split[1] != 'CREATURE':
                        die("Not sure how to create new {}".format(split[1]))

                    if creating_creature:
                        die("Creating new creature without ending old "
                            "definition?")
                    current_creature = {}
                    creating_creature = True
                if split[0] == 'END':
                    if split[1] != 'CREATURE':
                        die("Not sure how to end def of {}".format(split[1]))
                    if not creating_creature:
                        die("Cannot end creature def without first starting"
                              " def")

                    verify_expected_args(current_creature)
                    creatures.append(current_creature)
                    creating_creature = False

            elif '=' not in line:
                print("What is this line: {} ?".format(line))
            else:
                split = line.split('=')
                current_creature[split[0]] = parse_arg(split[0], split[1])
            

    return creatures


def print_help(combat=False, attack=False):
    global COMBAT_COMMANDS
    global COMMANDS
    if combat:
        for name, what in COMBAT_COMMANDS.items():
            print(name)
            print('    ' + what)
    if attack:
        for name, what in ATTACK_COMMANDS.items():
            print(name, '\n    ', what);

    else:
        for name, what in COMMANDS.items():
            print(name)
            print("    " + what)

ATTACK_COMMANDS = {
    'list|show': "lists all of the creatures attacks and damage and info",
    "attack <weapon>": 
        "attack with the desired weapon, weapon can be either string or int",

    "heal-self <ammount>": "heal self by given ammount",
    "damage-self <ammount>": "damage self by specific ammount",
    "heal <creature name> <ammount>": "heal other creature by ammount",
    "damage <creature name> <ammount>": "damage other creature by ammount",

        
}

def combat_menu(creatures):
    """
        THis is similar to the main menu, in that the user can supply commands
        to the menu which have the desired effect, invalid commands should not
        break the program.

        This keeps track of whos turn it is, the health of all creatures and
        will 
    """

    def do_turn(creature):
        print("$$$ {} $$$".format(creature["NAME"]))
        while True:
            command = input("===>").strip()
            if command == 'exit':   break
            if not command:         continue
            if command == 'help':   print_help(attack=True)

            elif command in ['list', 'show']:
                print("{}, HP = {}".format(creature["NAME"], creature['HP']))
                print("Attacks:")
                for ii, attack in enumerate(creature['ATTACKS']):
                    print("{}    {}: dam: {}, + to hit: {}".format(ii,
                        attack['name'], attack['damage'], attack['to-hit']))
            else:
                split = command.split()
                if split[0] in ['heal-self', 'damage-self']:
                    if not split[1].isdigit():
                        print("arg 1 needs to be a digit")
                        continue
                    creature['HP'] += int(split[1]) if split[0] == 'heal-self'\
                                      else -int(split[1])

                elif split[0] == 'attack':
                    choice = split[1]
                    _a = [attack for attack in creature['ATTACKS']]
                    if choice.isdigit():
                        if int(choice) > len(creature['ATTACKS']) or        \
                           int(choice) < 0: print("Not in range!"); continue
                        print("Attacking with {}".format(
                            creature['ATTACKS'][int(choice)]))

                    elif choice in [aa['name'] for aa in _a]:
                        for each in _a:
                            if each['name'] == choice:
                                print("doing {} damage".format(each['damage']))


                    else:   print("invalid param for damage!"); continue



                    
                else: print("What?"); continue


    print("Entering combat with {} creatures!".format(len(creatures)))
    battle = True
    current = 0
    while battle:
        #print("{}'s turn".format(who))
        command = input("-->").strip()
        if not command:
            continue
        if 'help' in command:
            print_help(combat=True)
        elif command == "show" or command == 'list':
            for cre, hea in zip([creature["NAME"] for creature in creatures],
                                [creature["HP"] for creature in creatures]):
                print("{}: {}".format(cre, hea))
        elif command == 'purge':
            creatures = [creature for creature in creatures if 
                            creature['HP'] > 0]
        elif command == 'who' or command == 'turn':
            print("Currently it is {}'s turn".format(creatures[current]['NAME']))

        elif command == 'attack':
            do_turn(creatures[current])

        elif command == 'next':
            current = (current + 1) % len(creatures)
            print("Now it is {}'s turn".format(creatures[current]['NAME']))

        elif command == 'quit' or command == 'exit':
            break

        else:
            split = command.split()
            if split[0] == 'damage':
                if len(split) != 3:
                    print("invalid # of args for damage command")
                    continue
                if split[1] not in [creature["NAME"] for creature in creatures]:
                    print("{} is not in the creatures list".format(split[1]))
                    continue
                if not split[2].isdigit():
                    print("3rd param must be an int")
                    continue
                #probably a more clever way to do this
                for creature in creatures:
                    if creature['NAME'] == split[1]:
                        creature["HP"] -= int(split[2])

            elif split[0] == 'heal':
                if len(split) != 3:
                    print("invalid # of args for damage command")
                    continue
                if split[1] not in [creature["NAME"] for creature in creatures]:
                    print("{} is not in the creatures list".format(split[1]))
                    continue
                if not split[2].isdigit():
                    print("3rd param must be an int")
                    continue
                #probably a more clever way to do this
                for creature in creatures:
                    if creature['NAME'] == split[1]:
                        creature["HP"] += int(split[2])

                   
            elif split[0] == 'kill':
                if len(split) != 2:
                    print("Need to supply name of creature to kill!")
                    exit()
                if split[1] not in [creature["NAME"] for creature in creatures]:
                    print("{} is not in the creatures list".format(split[1]))
                    continue
                creatures = [creature for creature in creatures if
                             creature["NAME"] != split[1]]
            else:
                print("What?")



        
        

def start_combat(files):
    """
        wrapper function that grabs all of the creatures from all of the config
        files and then sorts all of these creatures by initiative and passes
        that sorted list of dictrs into the combat menu funciton (which is the
        actual implementation of combat)
    """
    creatures = []
    for _file in files:
        creatures += parse_config_file(_file)
    
    combat_menu(sort_by_initiative(roll_for_initiative(creatures)))

def main_menu(files=None):

    print("Run 'help' for help")
    files = []
    while True:
        command = input('>>>').strip()
        if command == '':
            continue
        if command == 'help':
            print_help()
        elif command == 'exit':
            break
        elif command == 'list':
            print(', '.join(files))
        elif command == 'start':
            if len(files) == 0:
                print("Need at least one file loaded to enter combat..")
            else:
                start_combat(files)
        else:
            split = command.split()
            if len(split) <= 1:
                print("What?")
            elif split[0] == 'load':
                files += split[1:]
            elif split[0] == 'remove':
                if split[1] not in files:
                    print("could not find file '{}'".format(split[1]))
                else:
                    files.remove(split[1])
            elif split[0] == 'bash':
                os.system(split[1])
            elif split[0] == 'math':
                print(eval(' '.join(split[1:])))
            else:
                print("Unknown command '{}'".format(command))
             
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main_menu(files=sys.argv[1:])
    else:
        main_menu()
