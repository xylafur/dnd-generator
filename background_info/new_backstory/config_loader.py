"""

    ***************************************************************************
    **                                                                       **
    **  IF YOU READ THROUGH THE DEFAULT CONFIG FILE IT WILL EXPLAIN THE      **
    **  PARSER AND ITS GOAL IN DEPTH                                         **
    **                                                                       **
    **  I WOULD RECOMMEND READING IT BEFORE GOING THROUGH THE CODE           **
    **                                                                       **
    ***************************************************************************


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

ONLY_IF_FIELD = compile(r'\[(\S+) onlyif ([^\]]+)\]')
FIELD = compile(r'\[(\S+)\]')

def ensure_valid_config(config_file='default_backstory_config'):
    with open(config_file) as f:
        field = None
        found_field, last_field = False, False
        tot = 0

        for line in f:
            if not line or line[0] == '\n' or line[0] == '#':
                continue

            print(line)

            match = search(ONLY_IF_FIELD, line)
            if match:
                import pdb; pdb.set_trace()

            match = search(FIELD, line)
            if match:
                if last_field:
                    print("INVALID.  FOUND 2 FIELDS WITHOUT ANY VALUES")
                    return False

                else:
                    last_field = True
                    if found_field  and tot != 100:
                        print("ERROR, TOTAL NOT 100 FOR FIELD: {}".format(field))
                        print("ENTRIES ADDED UP TO: {}".format(tot))
                        return False
                    found_field = True

                    tot = 0
                    field = match.groups()[0]
                    continue

            last_field = False
            if line.split()[0] not in ['<', '>', '+', '-', 'if', 'else']:
                try:
                    tot += int(line.split()[0])
                except ValueError:
                    print("Expected int or valid symbol not: "
                          "{}".format(line.split()[0]))
            else:
                #TODO: Add better error checking for operators
                pass

    #if anyone knows a better fix for this.  Its annoying that I have to have
    #this both in the loop and then before I return.. Is there a better way?
    if found_field  and tot != 100:
        print("ERROR, TOTAL NOT 100 FOR FIELD: {}".format(field))
        print("ENTRIES ADDED UP TO: {}".format(tot))
        return False

    return True

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

            match = search(ONLY_IF_FIELD, line)
            if match:
                current_field = match.groups()[0]
                fields[current_field] = {'percentages': [],
                                         'modifiers': {'+': [], '-': []},
                                         'extra': {'>': [], '<': []},
                                         'cond': {'if': None, 'else': None},
                                         'tot': 0, 'onlyif': match.groups()[1]}
                continue

            match = search(FIELD, line)
            if match:
                current_field = match.groups()[0]
                fields[current_field] = {'percentages': [],
                                         'modifiers': {'+': [], '-': []},
                                         'extra': {'>': [], '<': []},
                                         'cond': {'if': None, 'else': None},
                                         'tot': 0, 'onlyif': None}
                continue

            if not current_field:
                continue

            line = line.strip().split()


            #TODO: Add parsing for these value
            if line[0] in ['+', '-']:

                fields[current_field]['modifiers'][line[0]].append(
                    ' '.join(line[1:]).strip())

            elif line[0] in ['<', '>']:
                fields[current_field]['extra'][line[0]].append(
                    ' '.join(line[1:]).strip())

            elif line[0] in ['if', 'else']:
                fields[current_field]['cond'][line[0]] = \
                    ' '.join(line[1:]).strip()


            else:
                fields[current_field]['percentages'].append([int(line[0]),
                                                            ' '.join(line[1:])])

    return fields

if __name__ == '__main__':
    if ensure_valid_config():
        fields = load_config_to_dict()
    else:
        exit()

    print("TEST SUCCESS")
