'''
Created on Aug 20, 2011

@author: Shaun Patterson
'''

import curses
from editor.terminal.TerminalWindow import TerminalWindow
from editor import Formatting

class BufferTermWindow (TerminalWindow):
    def __init__(self, model):
        super().__init__ ()
        self.model = model
        
    def repaint (self):
        self.win.clear ()
        self.win.box ()
        
        self.format()
        
        # Draw the text
        x = 0
        y = 0 
        for line in self.displayedLines:
            self.win.addstr (y, x, line)
            y = y + 1
        
        self.win.refresh ()
        
    def format (self):
        self.displayedLines = Formatting.wordWrap (self.model.text, self.height - 1, self.width)
