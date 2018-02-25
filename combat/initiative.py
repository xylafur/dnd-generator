"""
    This is a module to keep track of the order of players in combat

    Eventually it will be used with other modules to form a full fledged combat
    module for the utility
"""
from lib.random_die import roll_d20

def creature_prompt(creatures, verbose=False):
    """
        Propmts the uiser for the name and initiative of a creature to add to 
        the dict of creatures that will be used in determining the order of
        attackers.
    """
    name = input("Enter the creature's name: ")
    initiative_text = "Enter the creature's initiative"
    if verbose:
        initiative_text += (", if you want the module to roll for them, simply "
                           "type roll and the module will roll a d20 for the "
                           "creature")
    initiative = input(initiative_text + ": ")

    creatures[name] = roll_d20() if 'roll' in initiative.lower() else int(initiative) 


def obtain_initiative(additional=True, creatures=None, verbose=False):
    """
        Obtains the initiative and names of all creatures entering battle

        Arguments:
            creatures(:class:`bool`): Optional dictonary containing creatures 
                                      and their names

            additional (:class:`bool`): will there be additional creatuires?

            verbose (:class:`bool`): verbose output 

        Note:
            If additional is true the functino will prompt the user for aditional
            creatures and their initiatives 
    """
    if creatures is None:
        creatures = {}

    if additional:
        prompt = "another creature?"
        if verbose:
            prompt += " (yes for another, no for no others)"
        while(True):
            creature_prompt(creatures, verbose=verbose)
            if 'n' in input(prompt + " ").lower():
                break
    return creatures

def sort_by_initiative(creatures):
    order = [(creature, initiative) for creature, initiative in creatures.items()]
    #bubble sort, I know its ineficient but it doesn't really matter
    #(don't tell leiss)
    for ii in range(len(order)):
        for jj in range(ii + 1, len(order)):
            if order[ii][1] < order[jj][1]:
                temp = order[ii]
                order[ii] = order[jj]
                order[jj] = temp
    return order

def initiative_tracker(additional=True, creatures=None, verbose=False):
    creatures = obtain_initiative(additional, creatures, verbose)
    order = sort_by_initiative(creatures)
    if verbose:
        print("listing out creatures in the order that they will attack.")
        print("Press enter to go to the next creature, type quit or stop to stop")
    ii = 0
    while True:
        print(order[ii % len(order)][0])
        response = input()
        if 'stop' in response or 'quit' in response:
            break
        ii+=1
