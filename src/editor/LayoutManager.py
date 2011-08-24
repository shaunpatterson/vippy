'''
Created on Aug 21, 2011

Tracks the layout of Windows on the screen

TODO: Needs to handle vertically split windows and horizontally split windows

@author: Shaun Patterson
'''

class LayoutManager(object):
    
    VARIABLE_SIZE = -1
    
    def __init__(self):
        self.layout = []
        
    def add (self, window, width, height):
        self.layout.append ((window, width, height))
    
    def find (self, window):
        pass
    
    def adjustLayout (self, width, height):
        ''' Readjust the layout for a new screen width / height '''
        x = 0 
        y = 0
        
        for windowLayout in self.layout:
            if isinstance (windowLayout, list):
                # Sub-layout, adjust this as well '''
                #self._adjustLayoutList (window, x, y, width, height)
                pass
            else:
                # Adjust this Window
                (window, windowWidth, windowHeight) = windowLayout
                
                if (windowWidth == LayoutManager.VARIABLE_SIZE):
                    windowWidth = width
                if (windowHeight == LayoutManager.VARIABLE_SIZE):
                    windowHeight = height - 3                                                            
                
                window.adjust (x, y, windowWidth, windowHeight) 
        
            
    def _adjustLayoutList (self, list, x, y, width, height):
        pass
        #for window in self.layout:
        #    if isinstance (window, list):
        #        # Sub-layout, adjust this as well '''
        #        self._adjustLayoutList (window, width, height)
        #    else:
        #        # Adjust this Window
        #        window.adjust (
                
    