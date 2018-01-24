""" This is a custom random class, it is supposed to extend functionality
    of the random module to make it easier for character generation
"""

import random

class InvalidRangeException(Exception):pass
class NoEventTriggeredException(Exception):pass


def within_range(number, range):
    """ Returns true if the number is within the range supplied 
        The range should either be a tuple or a list of size 2
    """
    if type(range) != list and type(range) != tuple:
        raise InvalidRangeException("Range should be of type tuple or list, "
                                    "It is of type {}".format(type(range)))
    if len(range) != 2:
        raise InvalidRangeException("Range should be of size 2")
    if range[0] > range[1]:
        raise InvalidRangeException("The first index of range should be smaller"
                                    " than or equal to the second")
    return number >= range[0] and number <= range[1]


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

def dice_roll(dice, number_dice=1, advantage=False, disadvantage=False):
    total = 0 
    for _ in range(number_dice):
        if advantage:
            total+= max(random.randint(1, dice), random.randint(1, dice)) 
        elif disadvantage:
            total+= min(random.randint(1, dice), random.randint(1, dice)) 
        else:
            total += random.randint(1, dice)
    return total
