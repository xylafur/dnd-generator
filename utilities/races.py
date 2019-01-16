
from random import choice

races = [
         "elf",
         "dwarf",
         "orc",
         "goliath",
         "human",
        ]


def choose_random_race():
    return choice(races)
