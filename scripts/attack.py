#!/bin/python3

from random import randint
from sys import argv

damage = {
        'longsword': lambda : randint(1, 8) + 2 + 2,
        'longbow': lambda : randint(1, 8) + 1,
        'handaxe': lambda : randint(1, 6) + 2,
    }

to_hit = {
        'longsword': 5 + 1,
        'longbow': 4,
        'handaxe': 5,
    }

def attack_main(*args, name="attack", **kwds):
    if len(args) == 1:
        weapon = args[0]
        print("To hit: {}, damage: {}".format(randint(1, 20) + to_hit[weapon],
                                              damage[weapon]()))
    else:
        print("usage: {} <weapon name>".format(name))
        print("Weapons:")
        for weapon in damage:
            print("    {}".format(weapon))

