'''
Created on Aug 16, 2011

@author: shaun
'''
from commands.Command import Command


class CountCommand(Command):
    def __init__ (self, value, previous_cmd):
        self.count = previous_cmd.count * 10 + int (value)
        print ("CountCommand: The count is now %d" % (self.count)) 
        
class PasteCommand(Command):  
    def execute (self):
        print ("PrintCommand is executing on %d lines" % (self.count))
        
class YankCommand(Command):
    def __init__ (self, value, previous_cmd):
        self.count = previous_cmd.count
        if self.count <= 0:
            self.count = 1
          
    def execute (self):
        print ("YankCommand is executing on %d lines" % (self.count))
        
    
        