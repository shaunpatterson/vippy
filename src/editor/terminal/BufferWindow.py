'''
Created on Aug 20, 2011

@author: Shaun Patterson
'''

import curses
from editor.Window import Window
from editor.TerminalWindow import TerminalWindow
from editor.terminal.StatusWindow import StatusWindow

class BufferWindow(TerminalWindow):
    def __init__(self, model):
        super().__init__ ()
        self.model = model
        
    def repaint (self):
        self.win.clear ()
        self.win.box ()
        self.win.addstr (0, 0, "Buffer Window", curses.A_STANDOUT)
        self.win.refresh ()
        
