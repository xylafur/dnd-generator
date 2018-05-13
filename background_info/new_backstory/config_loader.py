"""
    Module to load in backstory config files

    The expected format of the config files is:

        #COMMENTS

        [FIELDNAME]
        <probability as int> <sentence or word to be used if chosen>
        ...
        ...
        <probability as int> <sentence or word to be used if chosen>

        [FIELDNAME]
        <probability as int> <sentence or word to be used if chosen>
        ...
        ...
        <probability as int> <sentence or word to be used if chosen>

    If this is confusing, just check the default_backstory_config file and it
    will explain alot

"""
from re import search, compile

FIELD = compile(r'\[(\S+)\]')

def load_config_to_dict(config_file='default_backstory_config'):
    """
        Loads in a config file based on fields into a dict
    """
    fields = {}
    with open(config_file) as f:
        current_field = None

        for line in f:
            if line[0] == '#' or line == '\n' or not line:
                continue
            match = search(FIELD, line)
            if match:
                current_field = match.groups()[0]
                fields[current_field] = []
                continue

            if not current_field:
                continue

            line = line.strip().split()

            fields[current_field].append([int(line[0]), ' '.join(line[1:])])

    return fields

if __name__ == '__main__':
    print(load_config_to_dict())




