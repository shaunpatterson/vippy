'''
Created on Aug 17, 2011

@author: shaun
'''
from keymap.CommandDispatcher import CommandDispatcher

class ListCommandDispatcher(CommandDispatcher):
    ''' Command Dispatcher that does not execute the commands. Instead
         it appends the commands to a command list '''
    
    def __init__ (self):
        self.cmd_list = []
        
    def dispatch (self, cmd):
        self.cmd_list.append (cmd)
            
