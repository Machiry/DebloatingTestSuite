import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarExtractFile(TpcpTestCase):
        
    def setUp(self):
        # set the working path, be sure to change the path name here!
        workdirname = 'tar_tests'
        # set the features
        features = ['extract']
        # set up the test
        self.setUpTestFeatures(workdirname, features)
        
    ### define real tests below!
    
    # tests extracting from a known tar file and testing contents
    # tar --extract --file=test.tar
    def runTest(self):
        # copy files to temp dir
        subprocess.run(["cp", "./"+self._workdir+"test.tar", self._tmpdir.name])
        # run commands in temp dir
        os.chdir(self._tmpdir.name)
        # real test: extract, then cat extracted files to check correct extraction
        subprocess.run([self.exe,"--extract","--file=test.tar"])
        output = subprocess.run(["cat","file1.txt","file2.txt"], capture_output=True)
        self.assertBehavior(output.stdout, b'hello \nworld \n')

            
