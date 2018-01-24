""" Module to hold all of the functions called by parsers
"""
from background_info.life_story import generate_character_backstory
from background_info.namer import generate_name
from info.races import races
from lib.random_ext import dice_roll
from util.util import average_die
from util.char_gen_util import generate_character

generate_character = generate_character

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

