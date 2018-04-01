from testing.testing_util import test_assert, TestFailure, TestIncomplete
from character_generator.characters import Creature

def basic_creature_test():
    creat = Creature()
    test_assert(creat.strength != 0)

def fail_test():
    raise TestFailure()

def incomplete_test():
    raise TestIncomplete()
