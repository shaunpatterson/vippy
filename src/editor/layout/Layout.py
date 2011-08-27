'''
Created on Aug 21, 2011

@author: shaun
'''

import abc
from abc import ABCMeta

class Layout(metaclass=ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        self.layouts = []
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0
    
    def add (self, layout):
        ''' Add a Layout or Window object to this layout '''
        self.layouts.append (layout)
        
    def move (self, x, y):
        ''' Move the layout to a specific x y position '''
        self.x = x
        self.y = y
        self.reposition (x, y)
        
    def reposition (self, x, y):
        ''' Reposition everything in the layout according to a 
             new x,y position for the layout '''
        xOffset = x
        yOffset = y
        for layout in self.layouts:
            layout.move (xOffset, yOffset)
            yOffset = yOffset + layout.height
