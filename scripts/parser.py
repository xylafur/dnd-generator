#the expected arguments for each creature entry in a config file
CREATURE_EXPECTED_ARGS = ["NAME", "TOKEN", "INITIATIVE", "ATTACKS", "MOVEMENT",
                          "HP", "AC"]
GROUP_EXPECTED_ARGS = CREATURE_EXPECTED_ARGS[:] + ['COUNT']

def die(*args):
    """
        print args and then exit
    """
    for each in args:
        print(each)
    print("exiting..")
    exit()

def verify_expected_args(creature, _type='SINGLE'):
    if _type == "SINGLE":
        global CREATURE_EXPECTED_ARGS
        for arg in CREATURE_EXPECTED_ARGS:
            if arg not in creature.keys():
                die("Was not able to find arg {} in creature def".format(arg))
    elif _type == 'GROUP':
        global GROUP_EXPECTED_ARGS
        for arg in GROUP_EXPECTED_ARGS:
            if arg not in creature.keys():
                die("Was not able to find arg {} in creature def".format(arg))

    else:
        print("What is {}?".format(_type))
        exit()

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
    creating_creature = creating_group = False
    with open(filename) as f:
        current_creature = {}
        for line in [_line.strip() for _line in f]:
            if not line or len(line) == 0:
                continue

            if line[0] == '@':
                split = line[1:].split()
                if split[0] == 'NEW':
                    if creating_creature or creating_group:
                        die("Creating new creature without ending old "
                            "definition?")

                    current_creature = {}

                    if split[1] == 'CREATURE':
                        creating_creature = True
                        current_creature['type'] = 'single'

                    elif split[1] == 'CREATURE-GROUP':
                        creating_group = True
                        current_creature['type'] = 'group'

                    else:
                        die("Not sure how to create new {}".format(split[1]))

                if split[0] == 'END':
                    if not creating_creature and not creating_group:
                        die("Cannot end creature def without first starting"
                              " def")

                    if split[1] == 'CREATURE' and creating_creature:
                        verify_expected_args(current_creature)
                        creatures.append(current_creature)
                        creating_creature = False

                    elif split[1] == 'CREATURE-GROUP' and creating_group:
                        verity_expected_args(current_creature, _type='GROUP')
                        creatures.append(current_creature)
                        creating_group = False

                    else:
                        die("Not sure how to end def of {}".format(split[1])
                            + "creating group: {}, creating single: {}".format(
                                creating_creature, creating_group))


            elif '=' not in line:
                print("What is this line: {} ?".format(line))
            else:
                split = line.split('=')
                current_creature[split[0]] = parse_arg(split[0], split[1])
            

    return creatures


