'''
Created on Aug 16, 2011

@author: shaun
'''
from keymap.NormalMode import NormalMode

class CommandStateTest(object):

    def __init__(self, cmdString):
        self.cmds = cmdString
        pass
    
    def run (self):
        normalMode = NormalMode()
        for cmd in self.cmds:
            normalMode.handleKey(cmd)
        

if __name__ == '__main__':
    #test = CommandStateTest ("10p123p901p")
    test = CommandStateTest ("yy")
    test.run ()

        