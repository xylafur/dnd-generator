from character_generator.characters import Creature

class TestFailure(Exception):pass

def test_assert(exp):
    if not exp:
        raise TestFailure()

def basic_creature_test():
    creat = Creature()
    test_assert(creat['strength'] != 0)

tests = []

def run_testing(which='all'):
    if which == 'all':
        pass
    
