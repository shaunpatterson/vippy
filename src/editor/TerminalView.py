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
from editor.terminal.BufferTermWindow import BufferTermWindow
from editor.terminal.CommandBarTermWindow import CommandBarTermWindow
from editor.terminal.StatusBarTermWindow import StatusBarTermWindow
from editor.terminal.TabTermWindow import TabTermWindow
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
        self.tabsWindow = TabTermWindow (['tab test1', 'tab test2'], 1)
        
        # Buffer windows setup
        self.bufferLayout = HorizontalLayout ()
        
        self.layoutLeftTop = HorizontalLayout ([BufferTermWindow (self.bufferLeftTop), StatusBarTermWindow (self.bufferLeftTop.statusBar)])
        self.layoutLeftBottom = HorizontalLayout ([BufferTermWindow (self.bufferLeftBottom), StatusBarTermWindow (self.bufferLeftBottom.statusBar)])
        self.layoutRight = HorizontalLayout ([BufferTermWindow (self.bufferRight), StatusBarTermWindow (self.bufferRight.statusBar)])
    
        self.horizontalLeft = HorizontalLayout ([self.layoutLeftTop, self.layoutLeftBottom])
        
        self.verticalSplit = VerticalLayout ([self.horizontalLeft, self.layoutRight])
        
        self.bufferLayout.add (self.verticalSplit)
    
        # Command window
        self.commandBar = CommandBar ()
        self.commandBarWindow = CommandBarTermWindow (None, 1)
 
        self.layout = HorizontalLayout ([self.tabsWindow, self.bufferLayout, self.commandBarWindow])
        
        self.layout.move (0, 0)
        self.layout.resize (self.screenWidth, self.screenHeight)
       
        self.bufferLeftTop.text.append ("Line 1")
        self.bufferLeftTop.text.append ("Line 2")
        self.bufferLeftTop.text.append ("Line 3")
        self.bufferLeftTop.text.append ("Line 4")
        self.bufferLeftTop.text.append ("")
        
        self.bufferLeftTop.text.append ('''And the Lord spake, saying, "First shalt thou take out the Holy Pin. Then, shalt thou count to three. No more. No less. Three shalt be the number thou shalt count, and the number of the counting shall be three. Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. Five is right out. Once at the number three, being the third number to be reached, then, lobbest thou thy Holy Hand Grenade of Antioch towards thy foe, who, being naughty in My sight, shall snuff it."''')
        
        
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
        
