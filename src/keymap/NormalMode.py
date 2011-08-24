'''
Created on Aug 16, 2011

@author: shaun
'''


from commands.Commands import PasteCommand, CountCommand, YankCommand, \
    DeleteCommand, NoOpCommand
from keymap.Mode import Mode
from keymap.Transition import Transition, RecursiveTransition


class NormalMode (Mode):

    def __init__(self):
        super().__init__ ()
        
        # All commands that are countable
        self.countable_cmds = {
                                'p' : Transition (PasteCommand()),
                                'y' : Transition (NoOpCommand(), { 'y' : Transition (YankCommand()) }), 
                                'd' : Transition (NoOpCommand(), { 'd' : Transition (DeleteCommand()) }),
                               }
        
        # Set up the initial state transitions
        self.initialState = {  
                                '0' : RecursiveTransition (CountCommand ()),
                                '1' : RecursiveTransition (CountCommand ()),
                                '2' : RecursiveTransition (CountCommand ()),
                                '3' : RecursiveTransition (CountCommand ()),
                                '4' : RecursiveTransition (CountCommand ()),
                                '5' : RecursiveTransition (CountCommand ()),
                                '6' : RecursiveTransition (CountCommand ()),
                                '7' : RecursiveTransition (CountCommand ()),
                                '8' : RecursiveTransition (CountCommand ()),
                                '9' : RecursiveTransition (CountCommand ()),
                              }
        self.initialState.update(self.countable_cmds)
    
        self.reset ()
        
    
