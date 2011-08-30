'''
Created on Aug 30, 2011

@author: Shaun Patterson
'''

import unittest
from editor import Formatting

class FormattingTest (unittest.TestCase):
    
    def setUp (self):
        pass
    
    def tearDown (self):
        pass
    
    def testWordWrap1 (self):
        test = []
        test.append ("Testing One Two Three");
        
        self.assertEqual(["Testing One Two Three"], Formatting.wordWrap (test, 1, 80))

    def testWordWrap2 (self):
        ''' Simple break at the end of 'One' '''
        rows = 5
        cols = 11
        
        test = []
        test.append ("Testing One Two Three");
                
        self.assertEqual(["Testing One", " Two Three"], Formatting.wordWrap (test, rows, cols))

    def testWordWrap3 (self):
        ''' Simple break at the end of 'One' '''
        rows = 1
        cols = 11
        
        test = []
        test.append ("Testing One Two Three");
                
        self.assertEqual(["Testing One"], Formatting.wordWrap (test, rows, cols))

    def testWordWrap4 (self):
        ''' Simple break at the end of 'One' '''
        rows = 5
        cols = 4
        
        test = []
        test.append ("Testing One 0123456789");
                
        self.assertEqual(["Test", "ing ", "One ", "0123", "4567"], Formatting.wordWrap (test, rows, cols))
