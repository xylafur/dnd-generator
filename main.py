#!/usr/bin/env python3

# imports 
from characters import *

def name_gen(argv):




    from namer import generate_name
    generate_name('', 1)

    pass


def Main():
    print('DnD tool generating characters')

    from os import sys.argv as argv
    utilities = {
        'namer':name_gen
    }

    if argv[1] not in utilities:
        raise Exception('Unsupported utility: '+argv[1])

    utilities[argv[1]](argv)

    pass

if _name__ == '__main__':
    Main()


