'''
Created on Aug 16, 2011

@author: shaun
'''
from commands.Command import Command

class NoOpCommand(Command):
    pass

class CountCommand(Command):
    def processContext (self, context):
        self.count = context.previousCmd.count * 10 + int (context.value)
        print ("CountCommand: Process Context %d" % self.count)
        
class CountableCommand(Command):
    ''' A 'countable' command - something that can be run x number of times
        or over x number of lines, etc. 
        Ex: 5dd  (Delete is a countable command) '''
    def processContext (self, context):
        self.count = context.previousCmd.count
        if self.count <= 0:
            self.count = 1
    
class PasteCommand(CountableCommand):
    def execute (self):
        print ("PrintCommand is executing on %d lines" % (self.count))
        
class YankCommand(CountableCommand):
    def execute (self):
        print ("YankCommand is executing on %d lines" % (self.count))
        
class DeleteCommand(CountableCommand):
    def execute (self):
        print ("DeleteCommand is executing on %d lines" % (self.count))
        
