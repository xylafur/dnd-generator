""" Module for util things, such as averaging dice
"""

import math

def average(list):
    return sum(list) / len(list)

def average_die(die):
    return math.floor(average(die))

