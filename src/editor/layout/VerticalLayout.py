'''
Created on Aug 22, 2011

@author: Shaun Patterson
'''
from editor.layout.Layout import Layout

class VerticalLayout(Layout):
    ''' VerticalLayout is a variable size layout that aligns
        layouts vertically from left to right '''
    
    def __init__(self):
        super().__init__ ()
        self.layouts = []
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0
        
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
            xOffset = xOffset + layout.width

    def isVariableSize (self):
        ''' A VerticalLayout is always variable size. '''
        return (True, True)
    

    def _calculateInternalDimensions (self, width, height):
        ''' Calculate the new dimensions for all internal layouts '''
        
        variableWidths = []
        remainingWidth = width
        
        for layout in self.layouts:
            (variableWidth, _) = layout.isVariableSize ()
            
            if variableWidth:
                variableWidths.append (layout)
            else:
                layout.resize (layout.preferredWidth, height)
                remainingWidth = remainingWidth - layout.width
                
        if len (variableWidths):
            self._resizeAdjustableWidths (variableWidths, height, remainingWidth)
            
        
    def _resizeAdjustableWidths (self, layouts, height, remainingWidth):
        widthEach = int (remainingWidth / len (layouts))
        
        for layout in layouts:
            layout.resize (widthEach, height)
            
        # Add any extra to the end (for odd/fractional sizing) 
        extra = remainingWidth - (widthEach * len (layouts))
        if extra > 0:
            layout.resize (widthEach + extra, height)
