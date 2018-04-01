#!/usr/bin/env python3

from random import randint as r
import time

D = lambda n : r(1,n)
DA = lambda n : max(D(n),D(n))
DD = lambda n : min(D(n),D(n))

rollers = {
    -1:DD,
     0:D,
     1:DA,
}

def DG(Dice=20, DC=10, amt=1, base=0, vantage=0, print_rolls=False):
    """
    Dice rolls against a goal such as AC

    args:
    Dice    - what dice number
    DC      - the goal to be greater than to beat
    amt     - amount of rolls
    vantage - advantage or disadv
    print_rolls - output rolls
    """
    roller = rollers[vantage]
    rolls = [roller(Dice)+base for i in range(amt)]
    successes = len([i for i in rolls if i > DC])

    if print_rolls:
        print(rolls)

    print('Successes = {} out of {} rolls for DC = {}'.format(successes, amt, DC))


def DGP(Dice=20, DC=10, amt=1, base=0, vantage=0):
    """
    Dice rolls against a goal such as AC
    default print_rolls
    """
    DG(Dice=Dice, DC=DC, amt=amt, base=base, vantage=vantage, print_rolls=True)


def read_creatures(init_file_nm, gen_init=False, vantage=0):
    creatures = []

    with open(init_file_nm) as f:
        for line in f:
            creatures.append(eval(line))

    if gen_init:
        operation = {
            -1: lambda c : c['init'] + DD(20),
             0: lambda c : c['init'] + D(20),
             1: lambda c : c['init'] + DA(20),
        }
        operation = operation[vantage]
        for c in creatures:
            c['init'] = operation(c)

    return creatures


players = []
enemies = []
people = []

POS = 0

def init(pfile='player_inits.csv', efile='encounter_inits.csv', gen_init=True, vantage=0):
    """
    args:
        pfile : player file
        efile : enemy file
        gen_init : generate initials
        vantage : vantage
    """
    global players, enemies, people

    players = read_creatures(pfile)
    enemies = read_creatures(efile, gen_init=gen_init,vantage=vantage)
    people = []
    people.extend(players)
    people.extend(enemies)

    people.sort(key = lambda p : (p['init'], p['name']))
    people = people[::-1]


def P(creatures):
    """
    This function prints a creature table
    args:
        creatures = creature table
    """
    fmt = '{{:0{}d}} -> {{}}'.format(len(str(len(creatures))))
    for i, p in enumerate(creatures):
        print(fmt.format(i, p))

def TP():
    """ This function peeks the next player turn. """
    p = people[POS]
    print("{}'s turn...".format(p['name']))

def T(turn_time=15):
    """
    This function performs the turn for current player
    then goes readies next player

    args:
        turn_time : default 15 seconds
    """
    TP()

    fmt = '\rtime left {{:0{}d}} s'.format(len(str(turn_time)))

    for i in range(turn_time, 0, -1):
        print(fmt.format(i),end='')
        time.sleep(1)

    print()
    N()

def N():
    """ This function increments POS to next player. """
    global POS
    POS = (POS + 1) % len(people)

def HPMOD(name, mod=0):
    """
    This function linearly searches for name and modifies health by mod
    args:
        name    name of creature
        mod     default 0
    """
    for p in people:
        if p['name'] == name:
            print('Before: ', p)
            p['hp'] += mod
            print('After : ', p)
            return

def HELP():
    """ Displays help message """
    print('variables = people, players, enemies')
    print('functions = init, T, TP, N, HELP, P, HPMOD')
    print('Dice roll = DA, D, DD, DG, DGP')

init()
