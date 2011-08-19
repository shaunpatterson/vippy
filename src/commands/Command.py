'''
Created on Aug 15, 2011

@author: shaun
'''

class Command(object):
    
    def __init__ (self, value=None, previousCmd=None):
        self.value = None
        self.count = 0
        
        if previousCmd != None:
            self.count = previousCmd.count
        
    def processContext (self, context):
        self.count = context.previousCmd.count
        self.value = context.value
        
    def execute (self):
        pass
    
        
