import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarListFile(TpcpTestCase):
        
    def setUp(self):
        # set the working path, be sure to change the path name here!
        workdirname = 'tar_tests'
        # set the features
        features = ['extract']
        # set up the test
        self.setUpTestFeatures(workdirname, features)
        
    ### define real tests below!
    
    # tests extracting from a known tar file and testing contents
    # tar -list --file=test.tar
    def runTest(self):
        # copy files to temp dir
        subprocess.run(["cp", "./"+self._workdir+"test.tar", self._tmpdir.name])
        # run commands in temp dir
        os.chdir(self._tmpdir.name)
        # real test: list files in an archive
        output = subprocess.run([self.exe,"--list","--file=test.tar"], capture_output=True)
        self.assertBehavior(output.stdout, b'file1.txt\nfile2.txt\n')

            
