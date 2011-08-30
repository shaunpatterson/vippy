'''
Created on Aug 20, 2011

@author: Shaun Patterson
'''

import curses
from editor.Window import Window
from editor.terminal.TerminalWindow import TerminalWindow

class TabTermWindow (TerminalWindow):
    def __init__(self, tabs, preferredHeight = 1):
        super().__init__(Window.VARIABLE_DIMENSION, preferredHeight)
        self.tabs = tabs

    def repaint (self):
        x = 0
        for tab in self.tabs:
            self.win.addstr (0, x, " %s " % tab, curses.A_STANDOUT)
            x = x + len (tab) + 2
        
        self.win.refresh () 
