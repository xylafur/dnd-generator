""" THis is the module that defines all of the characters and their atributes
"""
from character_generator.char_stats import *

class InvalidCreatureParameterException(Exception): pass
class Creature:
    def __init__(self, base_stats=None, level=1):
        self.level = level

        if isinstance(base_stats, dict):
            self.stats = {}
            for key, stat in zip(list(STAT_TYPES.keys()), base_stats):
                self.stats[key] = stat
        elif isinstance(base_stats, list):
            self.stats = base_stats
        elif base_stats is None:
            self.stats = generate_stats_roll()
        else:
            InvalidCreatureParameterException("Cannot parse ase_stats of type"
                                              "{}".format(type(base_state)))

        self.modifiers = calculate_stat_mod(self.stats)

        self.ac = calculate_base_ac(self.stats)

        self.health_die = '20' #there needs to be a function that can calc this

        self.max_hp = calculate_max_hp(self.stats, self.health_die, self.level)

    def __getattr__(self, attr):
        """
            Allows a user to grab the stat directly as if it were just another
            property of the object

            creature = Creature()
            creature.strength
        """
        if attr in self.__dict__.keys():
            return self.__dict__[attr]
        if attr in STAT_TYPES.keys():
            return self.stats[attr]

class Character(Creature):
    def __init__(self, *args, **kwds):
        self.abilities = None


class Wizard(Character):
    def __init__(self):
        self.spells = []
        self.spell_slots = 0

character_types = [
    #("Conjurer", Conjurer)
]


def generate_NPC(first_names, last_names):
    assert(first_names and last_names)
    assert(type(first_names)==list and type(last_names)==list)
    assert(all(type(p)==str for p in first_names))
    assert(all(type(p)==str for p in last_names))

    pass

    def set_modifiers(self, str, dex, con, wis, int, cha):
        self.str.set_modifier(str)
        self.dex.set_modifier(dex)
        self.con.set_modifier(con)
        self.wis.set_modifier(wis)
        self.int.set_modifier(int)
        self.cha.set_modifier(cha)
