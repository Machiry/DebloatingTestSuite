import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarCreateDirFile(TpcpTestCase):
        
    def setUp(self):
        # set the working path, be sure to change the path name here!
        workdirname = 'tar_tests'
        # set the features
        features = ['create']
        # set up the test
        self.setUpTestFeatures(workdirname, features)
        
    ### define real tests below!
    
    # tests extracting from a known tar file and testing contents
    # tar --create --file tmpfilesdir
    def runTest(self):
        # copy files to temp dir
        subprocess.run(["mkdir", "-p", self._tmpdir.name + "/tmpfilesdir"])
        subprocess.run(["cp", "./"+self._workdir+"file1.txt", self._tmpdir.name + "/tmpfilesdir"])
        subprocess.run(["cp", "./"+self._workdir+"file2.txt", self._tmpdir.name + "/tmpfilesdir"])
        # run commands in temp dir
        os.chdir(self._tmpdir.name)
        # real test: create tar from a dir of files, extract, cat and check contents are same
        subprocess.run([self.exe,"--create","--file","test.tar","tmpfilesdir/"])
        output = subprocess.run(["tar","--list","--file=test.tar"], capture_output=True)
        self.assertBehavior(output.stdout, b'tmpfilesdir/\ntmpfilesdir/file1.txt\ntmpfilesdir/file2.txt\n')

            
