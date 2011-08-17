'''
Created on Aug 16, 2011

@author: shaun
'''

class Transition(object):
    def __init__(self, value=None, next_state=None):
        self.value = value
        self.next_state = next_state
        
class RecursiveTransition(Transition):
    def __init__(self, value=None):
        self.value = value
