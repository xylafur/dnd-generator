""" This is a module to generate a random life backstory based on race 
"""
from random import choice, randint

from info.races import races
from lib.random_die import roll_event
from background_info.namer import generate_name
from background_info.backstory_generator import cause_of_death, get_life_events
from background_info.childhood import *

MALE = 1
FEMALE = 0

def generate_character_backstory(race=None, age=None, gender=None, name=None):
    gender_opt = 0
    if not gender:
        gender_opt = choice([MALE, FEMALE])
    if not race:
        race = choice(races)
    if not name:
        name = generate_name(race, gender_opt)
    if not age:
        age = randint(20, 100)
    
    #there is a personal decisions section that can be implemented later.. alot of work
    childhood = generate_childhood(race)
    life_events = get_life_events(age)

    return {
        'childhood': childhood, 'age': age, 'race': race, 'gender': gender, 
        'name': name, 'life_events': life_events
    }
