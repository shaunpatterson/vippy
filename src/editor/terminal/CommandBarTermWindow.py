'''
Created on Aug 20, 2011

@author: Shaun Patterson
'''

import curses
from editor.Window import Window
from editor.terminal.TerminalWindow import TerminalWindow

class CommandBarTermWindow (TerminalWindow):
    def __init__(self, model, preferredHeight = 1):
        super().__init__(Window.VARIABLE_DIMENSION, preferredHeight)
        self.model = model

    def repaint (self):
        self.win.addstr (0, 0, "Command Bar Window", curses.A_STANDOUT)
        self.win.refresh ()
