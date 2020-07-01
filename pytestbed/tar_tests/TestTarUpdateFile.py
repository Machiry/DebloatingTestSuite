import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarUpdateFile(TpcpTestCase):
        
    def setUp(self):
        # set the working path, be sure to change the path name here!
        workdirname = 'tar_tests'
        # set the features
        features = ['modify']
        # set up the test
        self.setUpTestFeatures(workdirname, features)
        
    ### define real tests below!
    
    # tests replacing of contents of a file inside the archive
    # tar --update -f test.tar file1.txt
    def runTest(self):
        # copy files to temp dir
        subprocess.run(["cp", "./"+self._workdir+"test.tar", self._tmpdir.name])
        with open(self._tmpdir.name+"/file1.txt", 'w') as f:
            f.write("This is new file1 text\n")
        # run commands in temp dir
        os.chdir(self._tmpdir.name)
        # real test: concat and extract, then cat extracted files to check correct extraction
        subprocess.run([self.exe,"--update", "-f","test.tar","file1.txt"])
        subprocess.run(["tar","--extract","--file=test.tar"])
        output = subprocess.run(["cat","file1.txt","file2.txt"], capture_output=True)
        self.assertBehavior(output.stdout, b'This is new file1 text\nworld \n')

            
