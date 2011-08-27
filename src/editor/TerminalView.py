'''
Created on Aug 20, 2011

@author: shaun
'''

from editor.Buffer import Buffer
from editor.CommandBar import CommandBar
from editor.LayoutManager import LayoutManager
from editor.StatusBar import StatusBar
from editor.layout.HorizontalLayout import HorizontalLayout
from editor.layout.VerticalLayout import VerticalLayout
from editor.terminal.BufferWindow import BufferWindow
from editor.terminal.CommandBarWindow import CommandBarWindow
from editor.terminal.StatusWindow import StatusWindow
from editor.terminal.TabsWindow import TabsWindow
import curses
import curses.wrapper

class TerminalView(object):
    def __init__(self):
        self.initializeScreen ()
        
        # Buffer setups
        self.bufferLeftTop = Buffer ()
        self.bufferLeftBottom = Buffer ()
        self.bufferRight = Buffer ()
        
        # Tab setup
        self.tabsWindow = TabsWindow (['tab test1', 'tab test2'], 1)
        
        # Buffer windows setup
        self.bufferLayout = HorizontalLayout ()
        
        self.layoutLeftTop = HorizontalLayout ([BufferWindow (self.bufferLeftTop), StatusWindow (self.bufferLeftTop.statusBar)])
        self.layoutLeftBottom = HorizontalLayout ([BufferWindow (self.bufferLeftBottom), StatusWindow (self.bufferLeftBottom.statusBar)])
        self.layoutRight = HorizontalLayout ([BufferWindow (self.bufferRight), StatusWindow (self.bufferRight.statusBar)])
    
        self.horizontalLeft = HorizontalLayout ([self.layoutLeftTop, self.layoutLeftBottom])
        
        self.verticalSplit = VerticalLayout ([self.horizontalLeft, self.layoutRight])
        
        self.bufferLayout.add (self.verticalSplit)
    
        # Command window
        self.commandBar = CommandBar ()
        self.commandBarWindow = CommandBarWindow (None, 1)
 
        self.layout = HorizontalLayout ([self.tabsWindow, self.bufferLayout, self.commandBarWindow])
        
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
        self.layout.repaint ()
        
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
        
