'''
Created on Aug 20, 2011

@author: shaun
'''

import abc
from keymap.Transition import RecursiveTransition
from commands.Command import Command
from keymap.CommandDispatcher import CommandDispatcher
from commands.Context import Context

class Mode (metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        self.commandDispatcher = CommandDispatcher ()
        self.currentState = None
        self.previousCmd = None
        self.initialState = None
    
    def nextState (self, transition):
        # This feels like a hack. There's got to be a way of defining the 
        #  transition recursively
        #
        # A surrogate dictionary looks like it would work... but
        #  this solution ultimately seems easier for the small 1 off cases
        #
        if isinstance (transition, RecursiveTransition):
            return
        
        self.currentState = transition.nextState
        if (self.currentState == None):
            self.reset ()

    def handleKey (self, key):
        ''' Process the next key and return the resulting command (if any) '''
        cmd = None
        
        if (key in self.currentState):
            # Grab the transition
            transition = self.currentState [key]
            cmd = transition.value
           
            # Decorate the command 
            cmd.processContext (Context (key, self.previousCmd))
            
            if transition.is_leaf ():
                # Last state for the sequence.  Dispatch and reset
                self.commandDispatcher.dispatch (cmd)              
                self.reset ()  
            else:
                self.previousCmd = cmd
                self.nextState (transition)
        else:
            print ("%s is not in the current mapping" % (key))
            self.reset()
            
        return cmd

    def reset (self):
        self.currentState = self.initialState
        self.previousCmd = Command ()
