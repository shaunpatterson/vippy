'''
Created on Aug 15, 2011

@author: shaun
'''

class Command(object):
    
    def __init__(self, value=None, previous_cmd=None):
        self.value = None
        self.count = 0
        
        if previous_cmd != None:
            self.count = previous_cmd.count
        
    
    def execute (self):
        pass
    
        