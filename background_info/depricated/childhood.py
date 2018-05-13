from lib.random_die import roll_event, roll_d100
from lib.exceptions import RaceNotSupportedException
from background_info.namer import generate_name

from background_info.depricated.childhood_data import *

def generate_birthplace():
    return roll_event(100, birthplaces)

def generate_number_siblings():
    return roll_event(10, number_siblings)

def generate_who_raised():
    return roll_event(100, family)

def generate_reason_for_parent_absense():
    return roll_event(4, reason_absent)

def generate_childhood_socioeconomic_status():
    return roll_event(18, family_lifestyle, low=3)

def generate_childhood_home(modifier=None):
    if modifier == None: 
        return roll_event(200, childhood_home, low=-100)
    return roll_event(100, childhood_home, modifier=modifier)

def generate_childhood_memories(modifier=None):
    if modifier == None: 
        return roll_event(200, childhood_memories, low=-100)
    return roll_event(100, childhood_memories, modifier=modifier)

def generate_parents(race):
    mother = None
    father = None
    parents_names = [None, None]
    result = roll_event(100, parents)

    if "don't" in result:
        return result
    if 'half' in race:
        human_parent = random.choice([0, 1])
        parents_names[human_parent] = generate_name('human', human_parent)

        if 'orc' in race:
            parents_names[not human_parent] = generate_name('orc', not human_parent)
        elif 'dwarf' in race:
            parents_names[not human_parent] = generate_name('dwarf', not human_parent)
        else:
            raise RaceNotSupportedException(race)
    else:
        for ii in range(2):
            parents_names[ii] = generate_name(race, ii)
    return ("Knew parents, they were "+parents_names[0]+" and "+parents_names[1])

def generate_childhood(race, eco_class=None, birthplace=None, who_raised=None, 
                       num_sibs=None, home=None):
    """ Generates a childhood for an character, you may supply some of the 
        arguments, all of the arguments or none of the arguments.  For aruments
        not supplied, a random value will be generated
    """
    childhood = {}
    if not eco_class:
        childhood['class'] = generate_childhood_socioeconomic_status()
    else:
        childhood['class'] = eco_class

    if not birthplace:
        childhood['birthplace'] = generate_birthplace()
    else:
        childhood['birthplace'] = birthplace

    if not who_raised:
        childhood['who_raised'] = generate_who_raised()
    else:
        childhood['who_raised'] = who_raised
    
    if not num_sibs:
        childhood['num_sibs'] = generate_number_siblings()
    else:
        childhood['num_sibs'] = num_sibs

    childhood['parents absense'] = generate_reason_for_parent_absense() if \
            "Mother and Father" in childhood['who_raised'] else None
    childhood['parents'] = generate_parents(race)
    modifier = childhood_home_modifiers[childhood['class']]

    if not home:
        childhood['home'] = generate_childhood_home(modifier=modifier)
    else:
        childhood['home'] = home

    childhood['memories'] = generate_childhood_memories(modifier=modifier)

    return childhood

