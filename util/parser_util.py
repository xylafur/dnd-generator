""" Module to hold all of the functions called by parsers, also has a utility 
    that calls them
"""
import argparse
from os import sys
from background_info.life_story import generate_character_backstory
from background_info.namer import generate_name
from info.races import races
from lib.random_ext import dice_roll
from util.util import average_die
from util.char_gen_util import generate_character


#imported from an external file
generate_character = generate_character

def get_parser(program=sys.argv[0]):
    program = sys.argv[0]
    parser = argparse.ArgumentParser(prog=program,
                                     description=program+' is a DnD toolkit')
    subparser = parser.add_subparsers(help='sub command help')

    # sub argument parser for namer utility
    namer_parser = subparser.add_parser('namer', help='namer help')
    namer_parser.set_defaults(which='namer')
    namer_parser.add_argument('-l', '--list', action='store_true', help='list supported races')
    namer_parser.add_argument('-n', '--num_names', action='store', type=int, default=1, help='number of names to generate')
    namer_parser.add_argument('-r', '--race', action='store', type=str, default='elf', help='race of names to generate, default=elf')
    namer_parser.add_argument('-g', '--gender', action='store', type=int, default=0, help='gender of names to generate, 0 being male, 1 being female')

    # sub arugment parser for char gen
    char_parser = subparser.add_parser('chargen', help='namer help')
    char_parser.set_defaults(which='chargen')
    char_parser.add_argument('-p', action='store', type=int, default=1)

    # dice utility parser
    dice_parser = subparser.add_parser('diceroll', help='diceroll help')
    dice_parser.set_defaults(which='diceroll')
    dice_parser.add_argument('dice', metavar='D', type=int, nargs='+',
                    help='Highest number on the die you want to roll')
    dice_parser.add_argument('-n', '--number', action='store', type=int, 
                             default=1, help="number dice to roll")


    # module for averagin die
    avg_parser = subparser.add_parser('avg', help='avg help')
    avg_parser.set_defaults(which='avg')
    avg_parser.add_argument('die', metavar='D', type=int, nargs='+',
                            help="give a list of die, will return the averate")

    # stat parser
    stat_parser = subparser.add_parser('stats', help='stat help')
    stat_parser.set_defaults(which='avg')

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

utils = {
        'namer': namer_util,
        'chargen': generate_character,
        'diceroll': dice_util,
        'avg': avg_util,
    }

def parser_util(util, args):
    """ function that calls all other util funcitons, either from the command
        line or from the interactive shell
    """
    utils[util](args)
