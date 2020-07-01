import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarDeleteFile(TpcpTestCase):
        
    def setUp(self):
        # set the working path, be sure to change the path name here!
        workdirname = 'tar_tests'
        # set the features
        features = ['remove']
        # set up the test
        self.setUpTestFeatures(workdirname, features)
        
    ### define real tests below!
    
    # tests deleting a file inside the archive
    # tar --delete --file=test.tar file1.txt
    def runTest(self):
        # copy files to temp dir
        subprocess.run(["cp", "./"+self._workdir+"test.tar", self._tmpdir.name])
        # run commands in temp dir
        os.chdir(self._tmpdir.name)
        # real test: concat and extract, then cat extracted files to check correct extraction
        subprocess.run([self.exe,"--delete","--file=test.tar","file1.txt"])
        subprocess.run(["tar","--extract","--file=test.tar"])
        self.assertBoolean(not os.path.isfile(self._tmpdir.name + '/file1.txt'))
        self.assertBoolean(os.path.isfile(self._tmpdir.name + '/file2.txt'))
        output = subprocess.run(["cat","file2.txt"], capture_output=True)
        self.assertBehavior(output.stdout, b'world \n')

            
