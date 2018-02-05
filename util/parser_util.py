""" Module to hold all of the functions called by parsers, also has a utility 
    that calls them
"""
import argparse
from os import sys
from random import randint

from character_generator.char_stats import generate_stats_roll, calculate_stat_mod, calculate_base_AC, calculate_max_hp
from info.races import choose_random_race
from background_info.life_story import generate_character_backstory
from background_info.namer import generate_name
from info.races import races
from lib.random_ext import dice_roll
from util.util import average_die

# Function mapping of specific parts of the NPC.
# TODO: Redo with class based inheritance on the stats.  This is clunky.
CHARACTER = {'Name': '',
             'Gender': '',
             'Race': '',
             'Background': '',
             'Stats': '',
             'Stat Modifier': '',
             'Base AC': '',
             'Maximum HP': '',
            }

#we can add a config file that can create this dict at runtime from file
parsers = {
    'namer': {
        'parser': {
            'args': ['namer'],
            'kwds': {
                'help':'namer help'
            }
        },
        'defaults':{
            'args': [],
            'kwds': {
                'which': 'namer'
            }
        },
        'arguments': [
            {
                'args': ['-l', '--list'],
                'kwds': {'action':'store_true', 'help': 'list supported races'}
            },
            {
                'args': ['-n', '--num_names'],
                'kwds': {'action': 'store', 'type': int, 'default': 1, 
                         'help': 'number of names to generate'}
            },
            {
                'args': ['-r', '--race'],
                'kwds': {'action': 'store', 'type': str, 'default': 'elf', 
                         'help': 'race of names to generate, default=elf'}
            },
              {
                'args': ['-g', '--gender'],
                'kwds': {'action': 'store', 'type': int, 'default': 0, 
                         'help': 'gender of names to generate, 0 '
                                  'being male, 1 being female'}
            },
     ],
     #these are for use by the cli
     'args': ['list', 'num_names', 'race', 'gender']
    },
    'chargen': {
        'parser': {
            'args': ['chargen'],
            'kwds': {'help': 'chargen help'}
        },
        'defaults':{
            'args': [],
            'kwds': {'which': 'chargen'}
        },
        'arguments': [
            {
                'args': ['-p'],
                'kwds': {'action': 'store', 'type': int, 'default': 1}
            },
     ],
    'args': []
    },
    'diceroll': {
        'parser': {
            'args': ['diceroll'],
            'kwds': {'help': 'diceroll help'}
        },
        'defaults':{
            'args': [],
            'kwds': {'which': 'diceroll'}
        },
        'arguments': [
            {
                'args': ['dice'],
                'kwds': {'metavar': 'D', 'type': int, 'nargs': '+', 
                         'help': 'Highest number on the die you want to roll'}
            },
            {
                'args': ['-n', '--number'],
                'kwds': {'action': 'store', 'type': int, 'default': 1, 
                         'help': "number dice to roll"}
            },

     ],
    'args': ['number']
    },
    'avg': {
        'parser': {
            'args': ['avg'],
            'kwds': {'help': 'avg help'}
        },
        'defaults':{
            'args': [],
            'kwds': {'which': 'avg'}
        },
        'arguments': [
            {
                'args': ['die'],
                'kwds': {'metavar': 'D', 'type': int, 'nargs': '+', 
                         'help': 'give a list of die, will return the average'}
            },
     ],
    'args': []
    },
#    'stats': {
#        'parser': {
#            'args': ['stats'],
#            'kwds': {'help': 'stat help'}
#        },
#        'defaults':{
#            'args': [],
#            'kwds': {'which': 'stat'}
#        },
#        'arguments': []
#    },
}

def get_parser(program=sys.argv[0]):
    program = sys.argv[0]
    parser = argparse.ArgumentParser(prog=program,
                                     description=program+' is a DnD toolkit')
    subparser = parser.add_subparsers(help='sub command help')

    for par in parsers:
        par = parsers[par]
        temp_parser = subparser.add_parser(*par['parser']['args'], 
                                           **par['parser']['kwds'])
        temp_parser.set_defaults(*par['defaults']['args'], 
                                 **par['defaults']['kwds'])
        for argument in par['arguments']:
            temp_parser.add_argument(*argument['args'], **argument['kwds'])

    return parser

def namer_util(args):
    if args.list:
        return 'Supported races: ' + str(races)
    result = []
    for n in range(args.num_names):
        result.append(generate_name(args.race, args.gender))
    return result

def chargen_util(args):
    return generate_life_story()

def dice_util(args):
    return dice_roll(args.dice[0])

def avg_util(args):
    return average_die(args.die)

def encounter_util(args):
    return generate_encounter(args.die)

def chargen_util(*args, **kwds):
    gender = randint(0, 1)
    CHARACTER['Race'] = choose_random_race()
    CHARACTER['Gender'] = 'Male' if gender else 'Female'
    CHARACTER['Name'] = generate_name(CHARACTER['Race'], gender)
    CHARACTER['Background'] = generate_character_backstory()
    CHARACTER['Stats'] = generate_stats_roll()
    CHARACTER['Stat Modifier'] = calculate_stat_mod(CHARACTER['Stats'])
    CHARACTER['Base AC'] = calculate_base_AC(CHARACTER['Stats'])

    # TODO: To be better determined base on a class, for now hardcoding.
    CHARACTER['Maximum HP'] = calculate_max_hp(CHARACTER['Stats'], 8, 4)

    result = []
    for key in CHARACTER:
        # Generate and print all the stats.
        result.append("{}: {}".format(key, CHARACTER[key]))
    return result

utils = {
        'namer': namer_util,
        'chargen': chargen_util,
        'diceroll': dice_util,
        'avg': avg_util
    }

def parser_util(who, util, args):
    """ function that calls all other util funcitons, either from the command
        line or from the interactive shell
    """
    result = utils[util](args)
    if not isinstance(result, list):
        result = [result] 
    if who == 'shell':
        return result
    for line in result:
        print(line)
