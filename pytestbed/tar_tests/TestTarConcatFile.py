import unittest
import subprocess
import os
import tempfile

from pytestbed.TpcpUnitTest import TpcpTestCase

class TestTarConcatFile(TpcpTestCase):
    
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
        self.features = ['modify']
        
    ### define real tests below!
    
    # tests extracting from a known tar file and testing contents
    # tar --concatenate --file=test.tar test2.tar
    def runTest(self):
        # copy files to temp dir
        subprocess.run(["cp", "./"+self._workdir+"test.tar", self._tmpdir.name])
        subprocess.run(["cp", "./"+self._workdir+"test2.tar", self._tmpdir.name])
        # run commands in temp dir
        os.chdir(self._tmpdir.name)
        # real test: concat and extract, then cat extracted files to check correct extraction
        subprocess.run([self.exe,"--concatenate","--file=test.tar","test2.tar"])
        subprocess.run([self.exe,"--extract","--file=test.tar"])
        output = subprocess.run(["cat","file1.txt","file2.txt","file3.txt","file4.txt"], capture_output=True)
        self.assertBehavior(output.stdout, b'hello \nworld \nThis is file3. \nThis is file4. \n')

            
