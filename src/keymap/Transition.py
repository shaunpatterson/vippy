'''
Created on Aug 16, 2011

@author: shaun
'''

class Transition(object):
    def __init__(self, value=None, nextState=None):
        self.value = value
        self.nextState = nextState
    
    def is_leaf (self):
        return (self.nextState == None)
        
class RecursiveTransition(Transition):
    def __init__(self, value=None):
        self.value = value
    
    def is_leaf (self):
        return False
