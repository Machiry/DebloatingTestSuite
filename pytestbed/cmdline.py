
import cProfile
import pstats

import os

import argparse
import configparser

from pytestbed.version import __version__
from pytestbed.TpcpUnitTest import TpcpTestCase, TpcpTestSuite, TpcpTestResult, TpcpTestRunner

# TODO: add the test suites below manually as they are created,
# unclear if there's a good way to do this automatically
import pytestbed.tar_tests
import pytestbed.chmod_tests

import unittest

###
# Process INI config file that describes batch mode
###

# TODO: make this more automatic, this is just for proof of concept
def tar_suite_features():
    return set(['extract', 'create', 'modify', 'remove'])

# process and return as a python dict of config
def process_ini(inifile):
    config = configparser.ConfigParser()
    config.read(inifile)
    
    testcases = {}
    
    for testcase in config.sections():
        testcases[testcase] = {}
        
        if 'original' not in config[testcase]:
            raise Exception
        
        # this is the original non-debloated executable that was used
        # to produce the executable that we are testing
        
        testcases[testcase]['original'] = config[testcase]['original']
        
        if 'suite' not in config[testcase]:
            raise Exception
        
        testcases[testcase]['suite'] = config[testcase]['suite']
        
        if 'included' not in config[testcase] and 'excluded' not in config[testcase]:
            raise Exception
        
        features_set = tar_suite_features()
        
        if 'included' in config[testcase]:
            included_list = (config[testcase]['included']).split(',')
            included_features = set([ x.strip() for x in included_list ])
            if 'all' in included_features:
                included_features = tar_suite_features()
            # include features only specifically defined from full set
            # intersection of two sets
            features_set = features_set & included_features
        
        if 'excluded' in config[testcase]:
            excluded_list = (config[testcase]['excluded']).split(',')
            excluded_features = set([ x.strip() for x in excluded_list ])
            # exclude the named features; overrides the included features if conflict
            # difference of two sets
            features_set = features_set - excluded_features
        
        testcases[testcase]['features'] = list(features_set)
        
        # if output file not given, then dump report to console
        
        if 'output' in config[testcase]:
            testcases[testcase]['output'] = config[testcase]['output']
        else:
            testcases[testcase]['output'] = ':CONSOLE'
            
        # TODO: run shell commands before running tests? to allow environment customization
        
        if 'prescript' in config[testcase]:
            testcases[testcase]['prescript'] = config[testcase]['prescript']
            
    return testcases

###
# Process command options and subcommands
###

def process_cmdline():
    version_txt = 'TPCP Testbed Runner Tool - v' + __version__
    parser = argparse.ArgumentParser(description=version_txt)
    parser.add_argument('--version', action='version', version='run_testbed.py --- '+version_txt)
    
    parser.add_argument('--batch', action='store', dest='ini_path', metavar='PATH', default=argparse.SUPPRESS, help='run testbed in batch mode on one or more executables, defined in an INI file')
    
    
    ### TODO: the following are deprecated options
    
    parser.add_argument('--chmod', action='store', dest='chmod_path', metavar='PATH', default=argparse.SUPPRESS, help='run chmod tests suite on a single executable at PATH (deprecated)')
    parser.add_argument('--tar', action='store', dest='tar_path', metavar='PATH', default=argparse.SUPPRESS, help='run tar tests suite on a single executable at PATH (deprecated)')
    
    args = parser.parse_args()
    # returns a dict of the args set
    return vars(args)

###
# Next actually run the tests
###

def run_testbed():
    args = process_cmdline()
    
    if args == {}:
        print("** No arguments provided! Canceling.")
        print("Please provide at least one test suite option to run.")
        print("Rerun with the -h or --help option to get a list of possible test suites and options.")
        
    for option in [key for key in args if '_path' in key]:
        # set the path then loop through all exes in that path
        path = args[option]
        # set the suite details
        suite = None
        if option == 'ini_path':
            # TODO: build up full test suite but proof of concept for now
            testcases = process_ini(path)
            for exe in testcases:
                suite = pytestbed.tar_tests.load_tests(exe, testcases[exe]['original'], testcases[exe]['features'])
                TpcpTestRunner(verbosity=2).run(suite)
        elif option == 'chmod_path':
            suite = pytestbed.chmod_tests.load_tests(path)
            TpcpTestRunner(verbosity=2).run(suite)
        elif option == 'tar_path':
            suite = pytestbed.tar_tests.load_tests(path)
            TpcpTestRunner(verbosity=2).run(suite)
        else:
            continue
        # run the tool automatically to generate 'debloated' executables
        #subprocess.run(["config['tool']['path']"], capture_output=True)
        #for executable in os.listdir(path):
            #print(executable)
            #suite.addTest(TpcpTestCase.parametrize(pymodulename, exe=executable))
        #TpcpTestRunner(verbosity=2).run(suite)
        #unittest.main(testRunner=TpcpTestRunner)
