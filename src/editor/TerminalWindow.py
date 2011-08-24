'''
Created on Aug 20, 2011

@author: shaun
'''

import abc
from abc import ABCMeta

import sys
import logging
import curses
from editor.Window import Window

logger = logging.getLogger(__name__)

class TerminalWindow(Window):
    
    @abc.abstractmethod
    def __init__(self, width = Window.VARIABLE_DIMENSION, height = Window.VARIABLE_DIMENSION):
        super().__init__ (width, height)
        
        # Create a 0x0 curses window.  The window position and size
        #  will be determined by the parenting layout
        self.win = curses.newwin (0, 0, 0, 0)
      
    def move (self, x, y):
        try:
            super().move (x, y)
            self.win.mvwin (y, x)
        except:
            # This'll throw exceptions when the window is not of the correct size, 
            #  not initialized, etc
            pass
            
        
    @abc.abstractmethod
    def repaint (self):
        self.win.redrawwin ()
        self.win.refresh ()
    
    def resize (self, width, height):
        super().resize (width, height)
        self.win.resize (height, width)
        
             
        
        
