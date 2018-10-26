from random import randint

skills = {
            'acrobatics': 4,
            'animal_handling': 6,
            'arcana': 3,
            'athletics': 5,
            'deception': 2,
            'history': 3,
            'insight': 3,
            'intimidation': 5,
            'investigation': 3,
            'medicine': 3,
            'nature': 3,
            'perception': 6,
            'performance': 2,
            'persuasion': 2,
            'religion': 3,
            'slieight_of_hand': 4,
            'stealth': 1,
            'survival': 6
        }

saving_throws = {
            'strength': 5,
            'dexterity': 1,
            'constitution': 6,
            'intelligence': 3,
            'wisdom': 3,
            'charisma': 2
        }

initiative = 1

def roll(skill=None):
    mod = 0
    if skill:
        mod = skills[skill]
    roll = randint(1, 20)

    print("{} roll is {} [raw: {}]".format(skill, roll + mod, roll))

def save(stat):
    roll = randint(1, 20)
    mod = saving_throws[stat]
    print("{} saving throw was {} [raw: {}]".format(stat, roll + mod, roll))

funcs = {'roll': roll, 'save': save}

def roll_main(*args, **kwds):
    if len(args) == 1:
        if args[0] in ['initiative', 'init']:
            print("initiative: {}".format(randint(1, 20) + initiative))
        elif args[0] in skills.keys():
            roll(args[1])
        elif args[0].isnumeric():
            print(randint(1, int(args[1])))
        else:
            print("{} is not a valid command".format(args[0]))

    elif len(args) == 2:
        if args[2] == 'save':
            save(args[1])
    else:
        roll()
