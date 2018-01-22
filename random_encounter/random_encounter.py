""" Module for generating random encounters

    So how I envision this to work is the entire party rolls for luck, and the 
    dm will also roll a luck check.  WHat the dm rolls will select a random 
    event table, with 20 possible events.  Then the dm will average all of the 
    player's luck rolls (unless one rolled a 20 or a 1, but now both, both would 
    cancel eachother out) and then use that average to select an event from in 
    the secondary tables.

    20 should be a really good thing that happens (like finding treasure) and a 
    1 should be a really bad thing (like being attacked by a strong ass monster)
"""

from random_encounter.random_encounter_tables import tables_manifest
from lib.random_die import roll_d20
from lib.util import average_die


def generate_encounter(players_rolls):

    print("generating encounter....")
    raise NotImplementedError()

    dm_roll = roll_d20()
    table = tables_manifest[dm_roll]

    return tables[average_die(players_roll)]
