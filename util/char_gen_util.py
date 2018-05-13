import character_generator.char_stats as stats

from background_info.depricated.life_story import generate_character_backstory
from background_info.namer import generate_name
from character_generator.char_stats import generate_stats_roll
from info.races import choose_random_race

from random import randint

# Function mapping of specific parts of the NPC.
# TODO: Redo with class based inheritance on the stats.  This is clunky.
CHARACTER = {}


def generate_character(*args, **kargs):
    """
        Generates a random npc with a backstory and stats.
    """
    # TODO: Do something with the arguments later.
    # TODO: This is admittedly awful.  This will be changed after we refine the libary.
    # It's currently here mostly for  testing purposes.
    gender = randint(0, 1)
    level = 4
    CHARACTER['Race'] = choose_random_race()
    CHARACTER['Gender'] = 'Male' if gender else 'Female'
    CHARACTER['Name'] = generate_name(CHARACTER['Race'], gender)
    CHARACTER['Background'] = generate_character_backstory()
    CHARACTER['Stats'] = generate_stats_roll()
    CHARACTER['Stat Modifier'] = stats.calculate_stat_mod(CHARACTER['Stats'])
    CHARACTER['Base AC'] = stats.calculate_base_ac(CHARACTER['Stats'])
    # Intelligence is for the wizard class, just using as a test.
    CHARACTER['Spell Save DC'] = \
        stats.calculate_spell_dc(CHARACTER['Stats']['Intelligence'], level)
    CHARACTER['Spell Attack Mod'] = \
        stats.calculate_spell_attack_mod(CHARACTER['Stats']['Intelligence'],
                                         level)


    # TODO: To be better determined base on a class, for now hardcoding.
    CHARACTER['Maximum HP'] = stats.calculate_max_hp(CHARACTER['Stats'], 8,
                                                     level)
    for key in CHARACTER:
        # Generate and print all the stats.
        print("{}: {}".format(key, CHARACTER[key]))
