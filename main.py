""" THis is the module that defines all of the characters and their atributes
"""

#list of tuples constaining (class name, construtor)
character_types = [
    ("Conjurer", Conjurer)
]

class Ability:
    def __init__(self, value, modifier=0):
        self.value = value 
        self.modifier = modifier

    def set_modifier(self, mod_val):
        this.modifier = modifier

#I couldn't think of a better way to do this..
class Abilities:
    def __init__(self, str, dex, con, wis, int, cha):
        self.str = Ability(str)
        self.dex = Ability(dex)
        self.con = Ability(con)
        self.wis = Ability(wis)
        self.int = Ability(int)
        self.cha = Ability(cha)

    def set_modifiers(self, str, dex, con, wis, int, cha):
        self.str.set_modifier(str)
        self.dex.set_modifier(dex)
        self.con.set_modifier(con)
        self.wis.set_modifier(wis)
        self.int.set_modifier(int)
        self.cha.set_modifier(cha)

class Character:
    def __init__(self):
        self.abilities = None


class Wizard(Character):
    def __init__(self):
        self.spells = []

class Conjurer(Wizard):
    pass 

