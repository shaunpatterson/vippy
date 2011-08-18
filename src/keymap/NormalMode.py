'''
Created on Aug 16, 2011

@author: shaun
'''

from commands.Command import Command

from keymap.Transition import Transition, RecursiveTransition
from commands.Commands import PasteCommand, CountCommand, YankCommand, DeleteCommand,\
    NoOpCommand
from commands.Context import Context
from keymap.CommandDispatcher import CommandDispatcher

class NormalMode(object):

    def __init__(self):
        
        self.command_dispatcher = CommandDispatcher ()
        
        
        # All commands that are countable
        self.__countable_cmds = {
                                'p' : Transition (PasteCommand()),
                                'y' : Transition (NoOpCommand(), { 'y' : Transition (YankCommand()) }), 
                                'd' : Transition (NoOpCommand(), { 'd' : Transition (DeleteCommand()) }),
                               }
        
        # Set up the initial state transitions
        self.__initial_state = {  
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
        self.__initial_state.update(self.__countable_cmds)
    
        self.reset ()
        
        
    def union (self, transition_list):
        result = {}
        for t in transition_list:
            result.update (t)
        return result
    
    
    def __next_state (self, transition):
        # This feels like a hack. There's got to be a way of defining the 
        #  transition recursively
        #
        # A surrogate dictionary looks like it would work... but
        #  this solution ultimately seems easier for the small 1 off cases
        #
        if isinstance (transition, RecursiveTransition):
            return
        
        self.__current_state = transition.next_state
        if (self.__current_state == None):
            self.reset ()
   
   
    def handle_key (self, key):
        ''' Process the next key and return the resulting command (if any) '''
        cmd = None
        
        if (key in self.__current_state):
            # Grab the transition
            transition = self.__current_state [key]
            cmd = transition.value
           
            # Decorate the command 
            cmd.process_context (Context (key, self.__previous_cmd))
            
            if transition.is_leaf ():
                # Last state for the sequence.  Dispatch and reset
                self.command_dispatcher.dispatch (cmd)              
                self.reset ()  
            else:
                self.__previous_cmd = cmd
                self.__next_state (transition)
                
        else:
            print ("%s is not in the current mapping" % (key))
            self.reset()
            
        return cmd
    
    def reset (self):
        self.__current_state = self.__initial_state
        self.__previous_cmd = Command ()
        print ("Reset!")
