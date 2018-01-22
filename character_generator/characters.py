""" THis is the module that defines all of the characters and their atributes
"""


class Character:
    def __init__(self):
        self.abilities = None


class Wizard(Character):
    def __init__(self):
        self.spells = []
        self.spell_slots = 0


class Conjurer(Wizard):
    def __init__(self):
        pass


character_types = [
    ("Conjurer", Conjurer)
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
