'''
Created on Aug 16, 2011

@author: shaun
'''

from commands.Command import Command

from keymap.Transition import Transition, RecursiveTransition
from commands.Commands import PasteCommand, CountCommand, YankCommand

class NormalMode(object):

    def __init__(self):
        
        # Todo: Having just the type in the transition table does not allow 
        #  passing in arguments -- for instance 'p' and 'P' are both pastes but
        #  it all depends on the direction
        
        self.__countableCmds = {
                                'p' : Transition (PasteCommand),
                                'y' : Transition (None, { 'y' : Transition (YankCommand) }), 
                                'd' : Transition (None, { 'd' : Transition (YankCommand) }),
                               }
        
        self.__initialState = {  
                                '0' : RecursiveTransition (CountCommand),
                                '1' : RecursiveTransition (CountCommand),
                                '2' : RecursiveTransition (CountCommand),
                                '3' : RecursiveTransition (CountCommand),
                                '4' : RecursiveTransition (CountCommand),
                                '5' : RecursiveTransition (CountCommand),
                                '6' : RecursiveTransition (CountCommand),
                                '7' : RecursiveTransition (CountCommand),
                                '8' : RecursiveTransition (CountCommand),
                                '9' : RecursiveTransition (CountCommand),
                              }
        self.__initialState.update(self.__countableCmds)

    
        self.reset ()
        
    def union (self, transitionList):
        result = {}
        for t in transitionList: 
            result.update (t)
        return result
    
    def __nextState (self, transition):
        # This feels like a hack. There's got to be a way of defining the 
        #  transition recursively
        if isinstance (transition, RecursiveTransition):
            return
        
        self.__currentState = transition.next_state
        if (self.__currentState == None):
            self.reset ()
            
    def handleKey (self, key):
        
        if (key in self.__currentState):
            # Grab the transition
            transition = self.__currentState [key]
            cmdType = transition.value
            if (cmdType != None):
                # Instantiate the type and execute the command
                cmd = cmdType(key, self.__previous_cmd)
                cmd.execute ()
                                
                self.__previous_cmd = cmd 
            
            self.__nextState (transition)
        else:
            print ("%s is not in the current mapping" % (key))
            self.reset()
        
        
    def reset (self):
        self.__currentState = self.__initialState
        self.__previous_cmd = Command ()
        print ("Reset!")
        
        
        
        
          
                                   
        