import time

from lib.random_die import roll_d, roll_d_adv, roll_d_dis

follers = {
    -1: roll_d_dis,
    0: roll_d,
    1: roll_d_adv
}

def dc_check(die=20, dc=10, amt=1, base=0, vantage=0, print_rolls=False):
    """
        Dice rolls against a goal such as AC

        args:
            die (:class:`int`): what dice number
            dc (:class:`int`): the goal to be greater than to beat
            amt (:class:`int`): amount of rolls
            vantage (:class:`int`): advantage or disadv
            print_rolls (:class:`int`): output rolls
    """
    roller = rollers[vantage]
    rolls = [roller(die)+base for i in range(amt)]
    successes = len([i for i in rolls if i > dc])

    if print_rolls:
        print(rolls)

    print('Successes = {} out of {} rolls for DC = {}'.format(successes, amt, DC))

def read_creatures(init_file_nm, gen_init=False, vantage=0):
    """
        Reads creatures in from a file, will generate initiative if specified

        Arguments:
            init_file_nm (:class:`str`): the path to the file

            gen_init (:class:`bool`): Should we generate initiative for the 
                                      creatures?
            
            vantage (:class:`int`): The level of advantage

        Returns:
            (:class:`dict`): dictionary of creatures and their information
    """
    creatures = []

    with open(init_file_nm) as f:
        for line in f:
            creatures.append(eval(line))

    if gen_init:
        operation = {
            -1: lambda c : c['init'] + roll_d_dis(20),
             0: lambda c : c['init'] + roll_d(20),
             1: lambda c : c['init'] + roll_d_adv(20),
        }
        operation = operation[vantage]
        for c in creatures:
            c['init'] = operation(c)

    return creatures

def init(pfile, efile, gen_init=True, vantage=0):
    """
        Initializes the combat sequence, reading in the players and enemies from
        their respective files and into variables that will be manipulated

        Arguments:
            pfile (:class:`str`): player file
            efile (:class:`str`): enemy file
            gen_init (:class:`bool`): generate initials?
            vantage (:class:`int`): level of advantage
    """
    players = read_creatures(pfile)
    enemies = read_creatures(efile, gen_init=gen_init, vantage=vantage)
    creatures= []

    creatures.extend(players)
    creatures.extend(enemies)

    creatures.sort(key = lambda p : (p['init'], p['name']))
    return creatures[::-1]

def print_creatures(creatures):
    """
        This function prints a creature table

        Arguments:
            creatures = creature dictinoary 
    """
    fmt = '{{:0{}d}} -> {{}}'.format(len(str(len(creatures))))
    for i, p in enumerate(creatures):
        print(fmt.format(i, p))

def run_turns(creatures):
    """
        function that continues until the user tells it to quit
        Allows the user to go through 
    """
    print("For all entries, hit enter to continue to the next or type in the amount to")
    print("change the creature's health by then enter to change it.  The change will be")
    print("printed and then the program will continue to the next player. "
          "If the creature")
    print("drops to or below 0 the creature will be removed from the list\n")
    while True:
        to_remove = []
        length = len(creatures)

        if length == 0:
            print("No more creatures")
            return

        for ii in range(length):
            c = creatures[ii]
            choice = input("{}: {}    ".format(c['name'], c['hp']))

            if 'q' in choice:
                return

            try:
                num = int(choice)
                creatures[ii]['hp'] += num
                if creatures[ii]['hp'] <= 0:
                    to_remove.append(ii)
            except ValueError:
                continue
        for ii in reversed(sorted(to_remove)):
            creatures.pop(ii)
        print()

def run_combat(player_file=None, enemy_file=None):
    """
        Main function for the combat utility
    """
    creatures = init(player_file, enemy_file)
    print_creatures(creatures)

    run_turns(creatures)
