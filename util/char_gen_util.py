from background_info.life_story import generate_character_backstory
from character_generator.char_stats import generate_stats_roll

CHARACTER = {'Background': '',
             'Stats': ''
             }


def generate_character(*args, **kargs):
    # TODO: Do something with the arguments later.
    CHARACTER['Background'] = generate_character_backstory()
    CHARACTER['Stats'] = generate_stats_roll()
    for key in CHARACTER:
        print("{}: {}".format(key, CHARACTER[key]))
