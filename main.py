#!/usr/bin/env python3
import argparse

from os import sys

from background_info.life_story import generate_life_story
from background_info.namer import generate_name
from races import races


def namer_util(args):
    if args.list:
        print('Supported races: ' + str(races))
        return

    for n in range(args.num_names):
        print(generate_name(args.race, args.gender))
    pass


def chargen_util(args):
    print(generate_life_story())


if __name__ == '__main__':
    prognm = sys.argv[0]

    parser = argparse.ArgumentParser(prog=prognm,
                                     description=prognm+' is a DnD toolkit')
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

    # fetch arguments
    args, leftovers = parser.parse_known_args()
    print(args)

    if len(sys.argv) <= 1:
        parser.print_help()
        parser.exit(1)

    # utility dictionary
    utils = {
        'namer': namer_util,
        'chargen': chargen_util
    }

    try:
        # call function
        if args.which in utils:
            utils[args.which](args)

    except AttributeError:
        parser.print_help()
        sys.exit(1)

    pass


