""" Hello, this is the main testing file for the DND Generator Utility

    This module is made to be super dynamic, when you create a new test, all you
    have to add it to the run pool is import the module into this file and then
    add that module into the 'test_modules' list.  After that the main testing
    function will call all of the functions in that module.

    That being said, make sure you only have tests in the module that you add
    
    The main testing function will run ANY functions in you module


    Eventually we could add support for this program to just grab all of the 
    modules from a testing file and do what the user has to do manually currently.

    tests_dict also needs to be implemented, basically a way to call a specific
    set of steps
"""
import testing.tests
from os import listdir
from imp import new_module
from importlib import import_module

from types import ModuleType
from testing.testing_util import TestFailure, TestIncomplete

#test_modules = [testing.character_tests]

tests_dict = {}#{'creature': creature_tests}

tests = []

def runtest(test):
    try:
        test()
        print("\033[1;32mSUCCESS\033[0m: ", end='')
    except TestFailure:
        print("\033[1;31mFAIL\033[0m: ", end='')
    except TestIncomplete:
        print("\033[1;34mINCOMPLETE\033[0m: ", end='')
    except Exception:
        pass
    print("{}".format(test.__name__))

def get_test_modules():
    test_files = listdir('testing/tests')
    return [import_module('testing.tests.' + file[:-3]) for file in \
            listdir('testing/tests')  if file[-3:] == '.py']

def run_testing(which='all'):
    test_modules = get_test_modules()
    tests = []

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
    
