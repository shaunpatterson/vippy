'''
Created on Aug 20, 2011

@author: shaun
'''

from editor.CommandBar import CommandBar
from editor.LayoutManager import LayoutManager
from editor.StatusBar import StatusBar
from editor.layout.HorizontalLayout import HorizontalLayout
from editor.terminal.BufferWindow import BufferWindow
from editor.terminal.CommandBarWindow import CommandBarWindow
from editor.terminal.StatusWindow import StatusWindow
from editor.terminal.TabsWindow import TabsWindow
import curses
import curses.wrapper
from editor.layout.VerticalLayout import VerticalLayout

class TerminalView(object):
    def __init__(self):
        self.initializeScreen ()
        
        # Tab setup
        self.tabsWindow = TabsWindow (['tab test1', 'tab test2'], 1)
        
        # Buffer windows setup
        self.bufferLayout = HorizontalLayout ()
        
        self.bufferWindowLeftTop = BufferWindow (None)
        self.bufferWindowLeftBottom = BufferWindow (None)
        self.bufferWindowRight = BufferWindow (None)
    
        self.horizontalLeft = HorizontalLayout ()
        self.horizontalLeft.add (self.bufferWindowLeftTop)
        self.horizontalLeft.add (self.bufferWindowLeftBottom)
        
        self.verticalSplit = VerticalLayout ()
        self.verticalSplit.add (self.horizontalLeft)
        self.verticalSplit.add (self.bufferWindowRight)
        
        self.bufferLayout.add (self.verticalSplit)
    
        # Status bar setup
        self.statusBar = StatusBar ()
        self.statusBarWindow = StatusWindow (self.statusBar, 1)
 
        # Command window
        self.commandBar = CommandBar ()
        self.commandBarWindow = CommandBarWindow (None, 1)
 
        self.layout = HorizontalLayout ()
        self.layout.add (self.tabsWindow)
        self.layout.add (self.bufferLayout)
        self.layout.add (self.statusBarWindow)
        self.layout.add (self.commandBarWindow)
        
        self.layout.move (0, 0)
        self.layout.resize (self.screenWidth, self.screenHeight)
        
        #self.resize ()
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
        self.bufferWindowLeftTop.repaint ()
        self.bufferWindowLeftBottom.repaint ()
        self.bufferWindowRight.repaint ()
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
        
