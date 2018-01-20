
def read_names(path_to_names='./assets/names.txt'):
    character_names = [[], []]
    with open(path_to_names) as names:
        character_names.extend(names.readline().split())
    return character_names


