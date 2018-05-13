""" Module to hold all of the functions called by parsers, also has a utility 
    that calls them
"""
import argparse
from os import sys

from background_info.depricated.life_story import generate_character_backstory
from background_info.namer import generate_name

from info.races import races

from lib.random_ext import dice_roll

from util.util import average_die
from util.char_gen_util import generate_character

from testing.testing_main import run_testing

from combat.initiative import initiative_tracker 
from combat.combat import run_combat

#imported from an external file
generate_character = generate_character

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
    'test':{
        'parser': {
            'args': ['test'],
            'kwds': {'help': 'test help'}
        },
        'defaults':{
            'args': [],
            'kwds': {'which': 'test'}
        },
        'arguments': [],
        'args': []
    },
    'initiative':{
        'parser': {
            'args': ['initiative'],
            'kwds': {'help': 'initiative help'}
        },
        'defaults':{
            'args': [],
            'kwds': {'which': 'initiative'}
        },
        'arguments': [],
        'args': []
    },
    'combat': {
        'parser': {
            'args': ['combat'],
            'kwds': {'help': 'combat help'}
        },
        'defaults':{
            'args': [],
            'kwds': {'which': 'combat'}
        },
        'arguments': [
            {
                'args': ['player_file'],
                'kwds': {'metavar': 'P', 'type': str, 
                         'help': 'The path to the file to use for characters'}
            },
            {
                'args': ['enemy_file'],
                'kwds': {'metavar': 'E', 'type': str, 
                         'help': 'The path to the file to use for enemies'}
            },
 
        ],
        'args': []
    }
}

def get_parser(program=sys.argv[0]):
    """
        Function that generates the command line parser for the program.

        Firstly it creates the base parser for the overall program and then
        creates all of the sub parsers for each of the utilities based on the
        parsers dictionary above.

        Hopefully eventually we can move the above dict into a file of some
        soft that can be open and parsed at runtime

        Arguments:

        Returns:
            (:class:`ArgumentParser`): An arg parse parser for the program

        Note:
            This funciton should automarically be used by the program.  TO add
            new entries into the parser there are 3 tings yoy must to

            1: Add the parser's info into the dict above
            2: Create a util function that will be called when the specific
               utiliy is to be invoked
            3: add a function pointer to that util function in the utils dict
               below

    """
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
        print('Supported races: ' + str(races))
        return

    for n in range(args.num_names):
        print(generate_name(args.race, args.gender))


def chargen_util(args):
    print(generate_life_story())

def dice_util(args):
    print(dice_roll(args.dice[0]))

def avg_util(args):
    print(average_die(args.die))

def encounter_util(args):
    print(generate_encounter(args.die))

def testing_util(args):
    print("running tests")
    run_testing()

def initiative_util(args):
    initiative_tracker()

def combat_util(args):
    run_combat(args.player_file, args.enemy_file)

utils = {
        'namer': namer_util,
        'chargen': generate_character,
        'diceroll': dice_util,
        'avg': avg_util,
        'test': testing_util,
        'initiative': initiative_util,
        'combat': combat_util
    }

def parser_util(util, args):
    """ function that calls all other util funcitons, either from the command
        line or from the interactive shell
    """
    utils[util](args)
