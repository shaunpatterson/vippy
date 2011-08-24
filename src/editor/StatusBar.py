'''
Created on Aug 20, 2011

@author: shaun
'''

class StatusBar(object):
    def __init__(self):
        pass
    
    def leftText (self):
        ''' Generate the text for the left side of the status bar '''
        return "[No Name][none, unix]"
    
    def rightText (self):
        ''' Generate the text for the right side fo the status bar '''
        return "[0,0/1 All]"
        