'''
Created on Aug 17, 2011

@author: shaun
'''

class Context(object):
    ''' Class used to pass previous context data from command to command
        or transition to transition '''
    
    def __init__ (self, value=None, prev_cmd=None):
        self.value = value
        self.prev_cmd = prev_cmd