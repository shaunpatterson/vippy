'''
Created on Aug 20, 2011

@author: Shaun Patterson
'''

import curses
import logging
from editor.Window import Window
from editor.terminal.TerminalWindow import TerminalWindow

logger = logging.getLogger(__name__)

class StatusBarTermWindow (TerminalWindow):
    def __init__(self, model, preferredHeight = 1):
        ''' Initialize the StatusBarTermWindow with a StatusBar model '''
        super().__init__ (Window.VARIABLE_DIMENSION, preferredHeight)
        self.model = model
    
    def repaint (self):
        try:
            self.win.clear ()

            # Draw the left text
            
            leftText = self.model.leftText ()
            leftPosition = 0
            self.win.addstr (0, leftPosition, leftText, curses.A_STANDOUT)
            
            rightText = self.model.rightText ()
            rightPosition = self.width - len (rightText) - 1
            self.win.addstr (0, rightPosition, rightText, curses.A_STANDOUT)

            self.win.refresh ()
            
        except Exception as e:
            logger.exception ("Error drawing status bar");
            raise
