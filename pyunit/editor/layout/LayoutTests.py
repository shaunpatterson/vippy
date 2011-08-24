'''
Created on Aug 21, 2011

@author: Shaun Patterson
'''
import unittest
from editor.layout.HorizontalLayout import HorizontalLayout
from editor.Window import Window

class LayoutTests(unittest.TestCase):

    class TestWindow(Window):
        def __init__ (self, preferredHeight = Window.VARIABLE_DIMENSION):
            super().__init__ (Window.VARIABLE_DIMENSION, preferredHeight)

        def move (self, x, y):
            self.x = x
            self.y = y

        def adjust (self, x, y, width, height):
            pass
        def repaint (self):
            pass
        def resize (self, width, height):
            super().resize (width, height)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIsVariableSize1 (self):
        hLayout = HorizontalLayout ()
        
        hLayout.add (LayoutTests.TestWindow ())
        hLayout.add (LayoutTests.TestWindow ())
        
        (variableWidth, variableHeight) = hLayout.isVariableSize()
        self.assertEqual (True, variableWidth)
        self.assertEqual (True, variableHeight)
        
    def testIsVariableSize2 (self):
        hLayout = HorizontalLayout ()
        
        # One or more fixed width -- this should be variable height
        hLayout.add (LayoutTests.TestWindow (1))
        hLayout.add (LayoutTests.TestWindow ())
        
        (variableWidth, variableHeight) = hLayout.isVariableSize()
        self.assertEqual (True, variableWidth)
        self.assertEqual (True, variableHeight)

    def testIsVariableSize3 (self):
        hLayout = HorizontalLayout ()
        
        hLayout2 = HorizontalLayout ()
        hLayout2.add (LayoutTests.TestWindow ())
        hLayout2.add (LayoutTests.TestWindow ())
        
        hLayout.add (hLayout2)
        
        (variableWidth, variableHeight) = hLayout.isVariableSize()
        self.assertEqual (True, variableWidth)
        self.assertEqual (True, variableHeight)

    def testIsVariableSize4 (self):
        hLayout = HorizontalLayout ()
        
        hLayout2 = HorizontalLayout ()
        hLayout2.add (LayoutTests.TestWindow (1))
        hLayout2.add (LayoutTests.TestWindow ())
        
        hLayout.add (hLayout2)
        
        (variableWidth, variableHeight) = hLayout.isVariableSize()
        self.assertEqual (True, variableWidth)
        self.assertEqual (True, variableHeight)

    def testIsVariableSize5 (self):
        hLayout = HorizontalLayout ()
        
        # Both windows are fixed height -- variable height should be false
        hLayout2 = HorizontalLayout ()
        hLayout2.add (LayoutTests.TestWindow (1))
        hLayout2.add (LayoutTests.TestWindow (1))
        
        hLayout.add (hLayout2)
        
        (variableWidth, variableHeight) = hLayout.isVariableSize()
        self.assertEqual (True, variableWidth)
        self.assertEqual (False, variableHeight)

    def testSimpleHorizonalLayout (self):
        mainLayout = HorizontalLayout ()
        
        test1 = LayoutTests.TestWindow ()
        test2 = LayoutTests.TestWindow (2)
        test3 = LayoutTests.TestWindow (3)
        
        mainLayout.add (test1)
        mainLayout.add (test2)
        mainLayout.add (test3)

        mainLayout.move (0, 0)        
        mainLayout.resize (100, 15)
       
        # Test widths
        self.assertEqual (100, mainLayout.width)
        self.assertEqual (100, test1.width)
        self.assertEqual (100, test2.width)
        self.assertEqual (100, test3.width)
        
        
        # Test heights
        self.assertEqual (10, test1.height)
        self.assertEqual (2, test2.height)
        self.assertEqual (3, test3.height)
        
        # Now test layout positions
        self.assertEqual (0, test1.x)
        self.assertEqual (0, test1.y)
        self.assertEqual (0, test2.x)
        self.assertEqual (10, test2.y)
        self.assertEqual (0, test3.x)
        self.assertEqual (12, test3.y)
        
        
    def testSimpleHorizonalLayout2 (self):
        mainLayout = HorizontalLayout ()
       
        bufferLayout = HorizontalLayout ()
        
        buffer1 = LayoutTests.TestWindow ()
        buffer2 = LayoutTests.TestWindow ()
        bufferLayout.add (buffer1)
        bufferLayout.add (buffer2)
        
        tabWindow = LayoutTests.TestWindow (1)
        commandBar = LayoutTests.TestWindow (1)
        
        mainLayout.add (tabWindow)
        mainLayout.add (bufferLayout)
        mainLayout.add (commandBar)
        
        mainLayout.move (0, 0) 
        mainLayout.resize (100, 16)

        self.assertEqual (100, mainLayout.width)
        self.assertEqual (100, bufferLayout.width)
        self.assertEqual (100, buffer1.width)
        self.assertEqual (100, buffer2.width)
        self.assertEqual (100, tabWindow.width)
        self.assertEqual (100, commandBar.width)
        
        self.assertEqual (14, bufferLayout.height)
        self.assertEqual (7, buffer1.height)
        self.assertEqual (7, buffer2.height)
        self.assertEqual (1, tabWindow.height)
        self.assertEqual (1, commandBar.height)
        
        self.assertEqual (0, tabWindow.x)
        self.assertEqual (0, tabWindow.y)
        self.assertEqual (0, bufferLayout.x)
        self.assertEqual (1, bufferLayout.y)
        self.assertEqual (0, buffer1.x)
        self.assertEqual (1, buffer1.y)
        self.assertEqual (0, buffer2.x)
        self.assertEqual (8, buffer2.y)
        self.assertEqual (0, commandBar.x)
        self.assertEqual (15, commandBar.y)
        

    def testSimpleHorizonalLayout3 (self):
        mainLayout = HorizontalLayout ()
       
        bufferLayout = HorizontalLayout ()
        
        buffer1 = LayoutTests.TestWindow (9)
        buffer2 = LayoutTests.TestWindow ()
        bufferLayout.add (buffer1)
        bufferLayout.add (buffer2)
        
        tabWindow = LayoutTests.TestWindow (1)
        commandBar = LayoutTests.TestWindow (1)
        
        mainLayout.add (tabWindow)
        mainLayout.add (bufferLayout)
        mainLayout.add (commandBar)
        
        tabWindow.height = 10
        commandBar.height = 10
        
        mainLayout.move (0, 0)
        mainLayout.resize (100, 16)
        
        self.assertEqual (14, bufferLayout.height)
        self.assertEqual (9, buffer1.height)
        self.assertEqual (5, buffer2.height)
        self.assertEqual (1, tabWindow.height)
        self.assertEqual (1, commandBar.height)

        self.assertEqual (0, tabWindow.x)
        self.assertEqual (0, tabWindow.y)
        self.assertEqual (0, bufferLayout.x)
        self.assertEqual (1, bufferLayout.y)
        self.assertEqual (0, commandBar.x)
        self.assertEqual (15, commandBar.y)

        self.assertEqual (0, tabWindow.x)
        self.assertEqual (0, tabWindow.y)
        self.assertEqual (0, bufferLayout.x)
        self.assertEqual (1, bufferLayout.y)
        self.assertEqual (0, buffer1.x)
        self.assertEqual (1, buffer1.y)
        self.assertEqual (0, buffer2.x)
        self.assertEqual (10, buffer2.y)
        self.assertEqual (0, commandBar.x)
        self.assertEqual (15, commandBar.y)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
