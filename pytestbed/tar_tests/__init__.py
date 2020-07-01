
from pytestbed.TpcpUnitTest import TpcpTestCase, TpcpTestSuite
import unittest

# TODO: is there a way to automatically import scenario classes?

from pytestbed.tar_tests.TestTarExtractFile import TestTarExtractFile
from pytestbed.tar_tests.TestTarGetFile import TestTarGetFile
from pytestbed.tar_tests.TestTarListFile import TestTarListFile
from pytestbed.tar_tests.TestTarConcatFile import TestTarConcatFile
from pytestbed.tar_tests.TestTarCreateFile import TestTarCreateFile
from pytestbed.tar_tests.TestTarCreateDirFile import TestTarCreateDirFile
from pytestbed.tar_tests.TestTarUpdateFile import TestTarUpdateFile
from pytestbed.tar_tests.TestTarDeleteFile import TestTarDeleteFile
from pytestbed.tar_tests.TestTarCompareFile import TestTarCompareFile

def load_tests(debloatpath, origpath, features):
    suite = TpcpTestSuite()
    suite.addTest(TestTarExtractFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarGetFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarListFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarConcatFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarCreateFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarCreateDirFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarUpdateFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarDeleteFile(features=features, exe=debloatpath, original=origpath))
    suite.addTest(TestTarCompareFile(features=features, exe=debloatpath, original=origpath))
    return suite




