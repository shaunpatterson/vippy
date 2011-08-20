'''
Created on Aug 17, 2011

@author: shaun
'''
from keymap.NormalMode import NormalMode
import unittest
from commands.Commands import YankCommand, DeleteCommand
from keymap.ListCommandDispatcher import ListCommandDispatcher

import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class Test(unittest.TestCase):

    def setUp(self):
        self.normalMode = NormalMode()
        self.normalMode.commandDispatcher = ListCommandDispatcher()

    def tearDown(self):
        self.normalMode = None

    
    def test_Yank1(self):
        ''' Test simple counted yank command '''
        cmds = "10yy"
        for cmd in cmds:
            self.normalMode.handleKey(cmd)
        
        results = self.normalMode.commandDispatcher.commandList
        self.assertEqual (len (results), 1)
        self.assertTrue (isinstance(results [0], YankCommand))
        self.assertEqual (10, results[0].count)
        
    def test_Yank2(self):
        cmds = "123yy"
        for cmd in cmds:
            self.normalMode.handleKey(cmd)
            
        results = self.normalMode.commandDispatcher.commandList
        self.assertEqual (len (results), 1)
        self.assertTrue (isinstance(results [0], YankCommand))
        self.assertEqual (123, results[0].count)
    
    def test_Delete1 (self):
        cmds = "dd"
        for cmd in cmds:
            self.normalMode.handleKey(cmd)
        
        results = self.normalMode.commandDispatcher.commandList
        self.assertEqual (len (results), 1)
        self.assertTrue (isinstance(results [0], DeleteCommand))
        self.assertEqual (1, results[0].count)
            
    def test_Delete2 (self):
        cmds = "987dd"
        for cmd in cmds:
            self.normalMode.handleKey(cmd)
        
        results = self.normalMode.commandDispatcher.commandList
        self.assertEqual (len (results), 1)
        self.assertTrue (isinstance(results [0], DeleteCommand))
        self.assertEqual (987, results[0].count)
        
        results[0].execute ()
            
            
        
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
