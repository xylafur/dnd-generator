from background_info.life_story import generate_character_backstory
from background_info.namer import generate_name
from character_generator.char_stats import generate_stats_roll
from character_generator.char_stats import calculate_stat_mod, calculate_base_AC, calculate_max_hp
from info.races import choose_random_race

from random import randint

# Function mapping of specific parts of the NPC.
# TODO: Redo with class based inheritance on the stats.  This is clunky.
CHARACTER = {'Name': '',
             'Gender': '',
             'Race': '',
             'Background': '',
             'Stats': '',
             'Stat Modifier': '',
             'Base AC': '',
             'Maximum HP': '',
            }


def generate_character(*args, **kargs):
    """
        Generates a random npc with a backstory and stats.
    """
    # TODO: Do something with the arguments later.
    # TODO: This is admittedly awful.  This will be changed after we refine the libary.
    # It's currently here mostly for  testing purposes.
    gender = randint(0, 1)
    CHARACTER['Race'] = choose_random_race()
    CHARACTER['Gender'] = 'Male' if gender else 'Female'
    CHARACTER['Name'] = generate_name(CHARACTER['Race'], gender)
    CHARACTER['Background'] = generate_character_backstory()
    CHARACTER['Stats'] = generate_stats_roll()
    CHARACTER['Stat Modifier'] = calculate_stat_mod(CHARACTER['Stats'])
    CHARACTER['Base AC'] = calculate_base_AC(CHARACTER['Stats'])

    # TODO: To be better determined base on a class, for now hardcoding.
    CHARACTER['Maximum HP'] = calculate_max_hp(CHARACTER['Stats'], 8, 4)
    for key in CHARACTER:
        # Generate and print all the stats.
        print("{}: {}".format(key, CHARACTER[key]))
