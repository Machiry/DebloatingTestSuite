import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarCreateDirFile(TpcpTestCase):
    
    @classmethod
    def setUpClass(cls):
        cls._originaldir = os.getcwd()
        cls._workdir = 'pytestbed/tar_tests/'
        cls._tmpdir = tempfile.TemporaryDirectory()
        
    @classmethod
    def tearDownClass(cls):
        # restore old working directory
        os.chdir(cls._originaldir)
        # remove the tmpdir
        cls._tmpdir.cleanup()
        
    def setUp(self):
        # reset dir, so we're not stuck in a non-existent temp dir
        os.chdir(self._originaldir)
        # set the features
        self.features = ['create']
        
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

            
