class SpelNotFoundException(Exception):pass

class Spell:
    def __init__(self, name, level, casting_time, range, components, duration, 
                 aoe, effects):
        """ Name <str>:         name of spell
            Level <int>:        spell level
            Casting time<str>:  how long to cast the spell
            Range<int>:         Range of the spell
            Components<str>:    Components required for the spell, verbal,
                                somatic, or material
            Duration<int>:      How long the spell lasts
            aoe<string>:        Area of effect, how the spell disperses, cube, 
                                sphere, cone, etc..
            effects<str>:       Description of the spell
        """
        self.name = name
        self.level = level
        self.casting_time = casting_time
        self.range = range
        self.components = components
        self.duration = duration
        self.aoe = aoe
        self.effects = effects

spells = {
    "thunderwave": {'casting_time': '1 action', 'range': 'self', 'aoe': None,
                    'components': 'Verbal/ somatic', 'duration': 'instantanious',
                    'effects': "A wave of thunderous force sweeps out from you. Each creature in a 15-foot cube originating from you must make a Constitution saving throw. On a failed save, a creature takes 2d8 thunder damage and is pushed 10 feet away from you. On a successful save, the creature takes half as much damage and isn't pushed. In addition, unsecured Objects that are completely within the area of effect are automatically pushed 10 feet away from you by the spell's effect, and the spell emits a thunderous boom audible out to 300 feet.At Higher Levels: When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 for each slot level above 1st."
    }
}

def generate_spell(name, level):
    """ Looks up a spell from the spells dictionary and creates it
    """
    if name in spells:
        return Spell(name, level, spells[name]['casting_time'], 
                     spells[name]['range'], spells[name]['components'], 
                     spells[name]['duration'], spells[name]['aoe'], 
                     spells[name]['effects'])
    else:
        raise SpellNotFoundException(name)
