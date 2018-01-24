from lib.random_die import roll_event, roll_d100

from background_generator.childhood_info import *

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
        return roll_event(200, childhood_home, low=-100)
    return roll_event(100, childhood_home, modifier=modifier)

def generate_parents():
    #TODO: Add support to where this will generate their names
    return roll_event(100, parents)

def generate_childhood():
    childhood = {}
    childhood['birthplace'] = generate_birthplace()
    childhood['who_raised'] = generate_who_raised()
    childhood['num_sibs'] = generate_number_siblings()
    childhood['parents absense'] = generate_reason_for_parent_absense() if \
            "Mother and Father" in childhood['who_raised'] else None
    childhood['parents'] = "You knew your parents" if \
            "Mother and Father" in childhood['who_raised'] else generate_parents() 
    childhood['class'] = generate_childhood_socioeconomic_status()
    modifier = childhood_home_modifiers[childhood['who_raised']]
    childhood['home'] = generate_childhood_home(modifier=modifier)
    childhood['memories'] = generate_childhood_memories(modifier=modifier)

    return childhood

