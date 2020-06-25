
from pytestbed.TpcpUnitTest import TpcpTestCase, TpcpTestSuite
import unittest

# TODO: is there a way to automatically import scenario classes?

from pytestbed.tar_tests.ScenarioTarStandard import standardScenario
from pytestbed.tar_tests.ScenarioTarDisableCreateTarballs import disableCreatingTarballsScenario

def load_tests(debloatpath, origpath, features):
    suite = standardScenario(debloatpath, origpath, features)
    #suite.addTest(disableCreatingTarballsScenario(path))
    return suite



