"""
    THis is the main module used for creating a backstory.

    First a config file is loaded into a dict via the config loader module then
    via random numbers a backstory is generated based on fields and options
    loaded in from that backstory config file.

    The backstory will be returned by this module as a dict
"""
from random import randint
from config_loader import load_config_to_dict

def select_field_by_percent(possible):
    """
        Generates a random number between 1 and 100, creates a running total
        from the percentages and then selects a value approprietly

        Arguments:
            possible: list of tuples
    """
    tot = 0
    val = randint(1, 100)

    for entry in possible:
        if tot <= val <= tot + entry[0]:
            return entry[1]

        tot += entry[0]

def generate_backstory(config_file='default_backstory_config'):
    """
        The main backstory function.  Gets the fields after loading in the
        config file and then selects a random value for each field and returns
        that result
    """
    fields = load_config_to_dict(config_file=config_file)

    backstory = {}

    for key, val in fields.items():
        backstory[key] = select_field_by_percent(val)

    return backstory


if __name__ == '__main__':
    print(generate_backstory())
