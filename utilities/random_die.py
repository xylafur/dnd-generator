from random import randint as r
import random

# roll functions
roll_d      = lambda n:r(1,n)   # roll a dice : [1,n]
roll_d0     = lambda n:r(0,n-1) # roll a dice : [0,n-1]
roll_d_adv  = lambda n:max(roll_d(n), roll_d(n))   # roll a dice with adv
roll_d0_adv = lambda n:max(roll_d0(n), roll_d0(n)) # roll a 0dice with adv
roll_d_dis  = lambda n:min(roll_d(n), roll_d(n)) # roll a dice with dis
roll_d0_dis = lambda n:min(roll_d(n), roll_d(n)) # roll a 0dice with dis

def roll_die(die, count=1, adv=False, dis=False, total=True):
    """
        Generates a random number between 1 and die value

        Args:
            die (:class: `int`) Upper bound of die rolls
        Kargs:
            count (:class: `int`) Number of dice rolls, default=1, if count==1
                returns a int instead of list

            adv (:class: `bool`):  If true, takes max of 2 rolls

            dis (:class: `bool`):  If True, generates two numbers and
                takes the smallest of the two.

            total (:class: `bool`):  If True, returns int sum of generated
                numbers. If False, returns list of length @count, of rolls

        Returns:
            int or list, see total parameter, if 
    """
    assert(die > 0)
    assert(count >= 1)

    if adv != dis:
        if adv: # advantage
            ret = [roll_d_adv(die) for i in range(count)]
        else:   # dis
            ret = [roll_d_dis(die) for i in range(count)]

    else: # advantage and disadvantage cancel out in 5e
        ret = [ roll_d(die) for i in range(count) ]

    return sum(ret) if (total or count==1) else ret

roll_d4 = lambda c, t=True: roll_die(4, count=c, total=t)
roll_d6 = lambda c, t=True: roll_die(6, count=c, total=t)
roll_d8 = lambda c, t=True: roll_die(8, count=c, total=t)
roll_d10 = lambda c, t=True: roll_die(10, count=c, total=t)
roll_d12 = lambda c, t=True: roll_die(12, count=c, total=t)
roll_d20 = lambda c, a=False, d=False, t=False: roll_die(20, c, a, d, t)
roll_d100 = lambda c, t=False: roll_die(20, count=c, total=t)

class NoEventTriggeredException(Exception):pass
def roll_event(dice, events, low=1, modifier=0):
    """ Function that will 'roll' a dir with `dice` sides and uses the events 
        argument to determine which event is selected

        Args:
            dice <int>: number of sides on dice to roll
            events <list<tuple<tuple>, <string>>>:
                list that contains tuples holding a range of values that will 
                trigger the event, and a string to return upon the event being 
                triggered.

                Example: [((0, 10), "Character dies"),
                         ((11, 20), "Character Lives"),
                         ...
                        ]
    """

    roll = random.randint(low, dice)
    roll += modifier
    for event in events:
        if within_range(roll, event[0]):
            return event[1]
    raise NoEventTriggeredException("The roll {} was not within the range of "
                                    "any events supplied to roll_event"
                                    .format(roll))
