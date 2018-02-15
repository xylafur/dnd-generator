import testing.character_tests 
from testing.testing_util import TestFailure

test_modules = [testing.character_tests]

tests_dict = {}#{'creature': creature_tests}

tests = []

def runtest(test):
    try:
        test()
        print("\033[1;32mSUCCESS\033[0m: ", end='')
    except TestFailure:
        print("\033[1;31mFAIL\033[0m: ", end='')
    except Exception:
        pass
    print("{}".format(test.__name__))

def run_testing(which='all'):
    tests = []
    #import pdb; pdb.set_trace()
    for module in test_modules:
        for obj in module.__dict__.values():
            if hasattr(obj, '__call__')                      \
            and obj.__module__ == module.__name__:
                tests.append(obj)

    if which == 'all':
        for test in tests:
            runtest(test)
    elif which in tests:
        tests_dict[which]()
    else:
        raise InvalidTestException("{} is not a valid test group".format(which))
    
