'''
Created on Aug 20, 2011

@author: Shaun Patterson
'''

import curses
from editor.Window import Window
from editor.TerminalWindow import TerminalWindow

class StatusWindow (TerminalWindow):
    def __init__(self, model, preferredHeight = 1):
        ''' Initialize the StatusWindow with a StatusBar model '''
        super().__init__ (Window.VARIABLE_DIMENSION, preferredHeight)
        self.model = model
    
    def repaint (self):
        self.win.clear ()

        # Draw the left text
        leftText = self.model.leftText ()
        leftPosition = 0
        self.win.addstr (0, leftPosition, leftText, curses.A_STANDOUT)
        
        rightText = self.model.rightText ()
        rightPosition = self.width - len (rightText) - 1
        self.win.addstr (0, rightPosition, rightText, curses.A_STANDOUT)
        
        self.win.redrawwin ()
        self.win.refresh ()
