'''
Created on Aug 20, 2011

@author: Shaun Patterson
'''

import abc
from abc import ABCMeta

import curses

class Window(metaclass=ABCMeta):
    
    # Variable width or height
    VARIABLE_DIMENSION = -1
    
    @abc.abstractmethod
    def __init__(self, preferredWidth = VARIABLE_DIMENSION, preferredHeight = VARIABLE_DIMENSION): 
        self.x = 0
        self.y = 0
        
        # Preferred dimensions of the window 
        self.preferredWidth = preferredWidth
        self.preferredHeight = preferredHeight
        
        # Calculated dimension of the window (this the actual width/height)
        self.width = preferredWidth
        self.height = preferredHeight
        
    @abc.abstractmethod
    def repaint (self):
        pass

    @abc.abstractmethod
    def move (self, x, y):
        self.x = x
        self.y = y
    
    def resize (self, width, height):
        self.width = width
        self.height = height
    
    def isVariableSize (self):
        return (self.preferredWidth == Window.VARIABLE_DIMENSION, 
                self.preferredHeight == Window.VARIABLE_DIMENSION)
