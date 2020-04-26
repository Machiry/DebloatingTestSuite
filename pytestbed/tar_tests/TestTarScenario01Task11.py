import unittest
import subprocess
import os
import tempfile

from pytestbed.UnitTest import TpcpTestCase

class TestTarScenario01Task11(TpcpTestCase):
    
    @classmethod
    def setUpClass(cls):
        cls._originaldir = os.getcwd()
        cls._workdir = 'tar_tests/'
        
    @classmethod
    def tearDownClass(cls):
        # restore old working directory
        os.chdir(cls._originaldir)
        
    def setUp(self):
        # reset dir, so we're not stuck in a non-existent temp dir
        os.chdir(self._originaldir)
        
    # define real tests below!
    # Test_11 tar --delete --file=test.tar Hello.txt
            
    def scenario01_task11(self):
        with tempfile.TemporaryDirectory() as directory:
            #print('The created temporary directory is %s' % directory)
            # copy files to temp dir
            subprocess.run(["cp", "./"+self._workdir+"file1.txt", directory])
            subprocess.run(["cp", "./"+self._workdir+"file2.txt", directory])
            subprocess.run(["cp", "./"+self._workdir+"exes/"+self.exe, directory])
            # run commands in temp dir
            os.chdir(directory)
            subprocess.run(["./"+self.exe,"--delete","--file=test.tar Hello.txt"])
            output = subprocess.run(["cat","file1.txt","file2.txt"], capture_output=True)
            self.assertEqual(output.stdout, b'hello \nworld \n')