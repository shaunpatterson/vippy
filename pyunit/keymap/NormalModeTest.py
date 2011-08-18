'''
Created on Aug 17, 2011

@author: shaun
'''
from keymap.NormalMode import NormalMode
import unittest
from commands.Commands import YankCommand
from keymap.ListCommandDispatcher import ListCommandDispatcher


class Test(unittest.TestCase):

    def setUp(self):
        self.normal_mode = NormalMode()
        self.normal_mode.command_dispatcher = ListCommandDispatcher()

    def tearDown(self):
        self.normal_mode = None

    
    def test_Yank1(self):
        ''' Test simple counted yank command '''
        cmds = "10yy"
        for cmd in cmds:
            self.normal_mode.handle_key(cmd)
        
        results = self.normal_mode.command_dispatcher.cmd_list
        self.assertEqual (len (results), 1)
        self.assertTrue (isinstance(results [0], YankCommand))
        self.assertEqual (10, results[0].count)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()