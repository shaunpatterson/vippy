'''
Created on Aug 20, 2011

@author: shaun
'''

import curses
import curses.wrapper
from editor.terminal.TabsWindow import TabsWindow
from editor.StatusBar import StatusBar
from editor.terminal.StatusWindow import StatusWindow
from editor.LayoutManager import LayoutManager
from editor.terminal.BufferWindow import BufferWindow
from editor.terminal.CommandBarWindow import CommandBarWindow
from editor.CommandBar import CommandBar
from editor.layout.HorizontalLayout import HorizontalLayout

class TerminalView(object):
    def __init__(self):
        self.initializeScreen ()
        
        # Tab setup
        self.tabsWindow = TabsWindow (['test1', 'test2'], 1)
        
        # Buffer window setup
        self.bufferWindow = BufferWindow (None)
        
        # Status bar setup
        self.statusBar = StatusBar ()
        self.statusBarWindow = StatusWindow (self.statusBar, 1)
 
        # Command window
        self.commandBar = CommandBar ()
        self.commandBarWindow = CommandBarWindow (None, 1)
 
        self.layout = HorizontalLayout ()
        self.layout.add (self.tabsWindow)
        self.layout.add (self.bufferWindow)
        self.layout.add (self.statusBarWindow)
        self.layout.add (self.commandBarWindow)
        
        self.layout.move (0, 0)
        self.layout.resize (self.screenWidth, self.screenHeight)
        
        self.repaint()
        
    def __del__ (self):
        curses.endwin ()
        
    def initializeScreen (self):
        self.screen = curses.initscr ()
        curses.start_color ()
        curses.noecho ()
        curses.cbreak ()
        (self.screenHeight, self.screenWidth) = self.screen.getmaxyx ()
        pass
        
    def repaint (self):
        self.screen.clear ()
        self.screen.refresh ()
        self.tabsWindow.repaint ()
        self.bufferWindow.repaint ()
        self.statusBarWindow.repaint ()
        self.commandBarWindow.repaint ()
        
    def resize (self):
        (self.screenHeight, self.screenWidth) = self.screen.getmaxyx ()
        self.layout.resize (self.screenWidth, self.screenHeight)
        self.repaint ()
         
    def run (self):
        while True: 
            ch = self.screen.getch ()
            if ch == curses.KEY_RESIZE:
                self.resize ()
            else:
                break
        
