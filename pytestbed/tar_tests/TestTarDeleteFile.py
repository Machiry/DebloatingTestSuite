import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarDeleteFile(TpcpTestCase):
    
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
        self.features = ['remove']
        
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

            
