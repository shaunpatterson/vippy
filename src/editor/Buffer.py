'''
Created on Aug 20, 2011

@author: shaun
'''
from editor.StatusBar import StatusBar
from editor import Formatting

class Buffer(object):
    def __init__(self, lines=[]):
        self.lines = lines
        
        # Create a status bar for the buffer
        self.statusBar = StatusBar ()
        
        self.text = []
        self.displayedLines = []
        
    def format (self):
        self.displayedLines = Formatting.wordWrap (self.text, self.width, self.height)
        
