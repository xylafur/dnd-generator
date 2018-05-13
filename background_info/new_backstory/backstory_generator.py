"""
    THis is the main module used for creating a backstory.

    First a config file is loaded into a dict via the config loader module then
    via random numbers a backstory is generated based on fields and options
    loaded in from that backstory config file.

    The backstory will be returned by this module as a dict
"""
from random import randint
from config_loader import load_config_to_dict

def select_field_by_percent(current, this, fields):
    """
        Generates a random number between 1 and 100, creates a running total
        from the percentages and then selects a value approprietly

        Arguments:
            possible: list of tuples
    """
    tot = 0
    val = randint(1, 100)

    for modifier, value in current['modifiers'].items():

        modifiers = []

        if not value or not modifier:
            break
        else:
            found_key = False

            for entry in value:
                for key in fields.keys():
                    if key in entry:
                        found_key = True
                        entry = entry.replace(key, str(fields[key]['tot']))

                modifiers.append(eval(entry))

        if modifier == '+':
            for add in modifiers:
                val += add
        elif modifier == '-':
            for sub in modifiers:
                val -= sub

    for extra, value in current['extra'].items():
        if not extra or not value:
            break

        if extra == '>':
            if val >= 100:
                return value
        elif extra == '<':
            if val <= 0:
                return value

    for cond, value in current['cond'].items():
        if not cond or not value:
            break

        if modifier == 'if':
            pass
        elif modifier == 'else':
            pass

    for entry in current['percentages']:
        if tot <= val <= tot + entry[0]:
            fields[this]['tot'] = val
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
        if not val['onlyif']:
            backstory[key] = select_field_by_percent(val, key, fields)
            continue

        for _key in fields.keys():
            if _key in val['onlyif']:
                val['onlyif'] = val['onlyif'].replace(_key,
                                                      str(fields[_key]['tot']))
        if eval(val['onlyif']):
            backstory[key] = select_field_by_percent(val, key, fields)

    return backstory




if __name__ == '__main__':
    print(generate_backstory())
