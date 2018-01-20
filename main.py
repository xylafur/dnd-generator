#!/usr/bin/env python3

# imports 
import argparse

def Main():
    print('DnD tool generating characters')

    from os import sys
    prognm = sys.argv[0]

    parser = argparse.ArgumentParser(prog=prognm,
                                     description=prognm+' is a DnD toolkit')
    subparser = parser.add_subparsers(help='sub command help')

    # sub argument parser for namer utility
    namer_parser = subparser.add_parser('namer', help='namer help')
    namer_parser.add_argument('-n', action='store', type=int, default=1)

    # sub arugment parser for char gen
    char_parser = subparser.add_parser('namer', help='namer help')
    char_parser.add_argument('-n', action='store', type=int, default=1)


    # test print
    print(parser.parse_args())

    pass

if __name__ == '__main__':
    Main()


