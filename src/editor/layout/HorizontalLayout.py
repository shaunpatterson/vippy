'''
Created on Aug 21, 2011

@author: Shaun Patterson
'''

import logging
from editor.layout.Layout import Layout

logger = logging.getLogger(__name__)

class HorizontalLayout(Layout):
    ''' HorizontalLayout is a variable size layout that stacks contained
         layouts horizontally on top of one another '''
    
    def __init__(self):
        super().__init__ ()
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
        
    def resize (self, width, height):
        ''' Resize this layout and then reposition everything inside '''
        self.width = width
        self.height = height

        self._calculateInternalDimensions (width, height)
        self.reposition (self.x, self.y)


    def reposition (self, x, y):
        ''' Reposition everything in the layout according to a 
             new x,y position for the layout '''
        xOffset = x
        yOffset = y
        for layout in self.layouts:
            layout.move (xOffset, yOffset)
            yOffset = yOffset + layout.height
        
    def isVariableSize (self):
        ''' A HorizontalLayout is always variable size. '''
        return (True, True)
    

    def _calculateInternalDimensions (self, width, height):
        ''' Calculate the new dimensions for all internal layouts '''
        
        variableHeights = []
        remainingHeight = height
        
        for layout in self.layouts:
            (_, variableHeight) = layout.isVariableSize ()
            
            if variableHeight:
                variableHeights.append (layout)
            else:
                layout.resize (width, layout.preferredHeight)
                remainingHeight = remainingHeight - layout.height
                
        if len (variableHeights):
            self._resizeAdjustableHeights (variableHeights, width, remainingHeight)
            
        
    def _resizeAdjustableHeights (self, layouts, width, remainingHeight):
        heightEach = int (remainingHeight / len (layouts))
        
        for layout in layouts:
            layout.resize (width, heightEach)
            
        # Add any extra to the end (for odd/fractional sizing) 
        extra = remainingHeight - (heightEach * len (layouts))
        if extra > 0:
            layout.resize (width, heightEach + extra)
    
