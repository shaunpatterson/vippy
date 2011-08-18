'''
Created on Aug 17, 2011

@author: shaun
'''

class CommandDispatcher(object):
    ''' Base command dispatcher.  All this class will do is execute 
         the command.  Subclass this class if more control is needed '''
    
    def __init__(self):
        pass
    
    def dispatch (self, cmd):
        cmd.execute ()
        