'''
Created on Aug 15, 2011

@author: shaun
'''

import logging.config

from editor.TerminalView import TerminalView

logging.config.fileConfig('logging.conf')
logger = logging.getLogger (__name__)


class Vippy:
    
    def __init__ (self):
        try:
            #__import__ ("pydevd")
            exec ("import pydevd")
            exec ("pydevd.settrace ()")
            #eval ("pydevd.settrace ()")
        except ImportError:
            pass
            
            
    
    def run (self):
        view = TerminalView ()
        view.run ()
        logger.debug ("Vippy has started")
        
    

if __name__ == '__main__':
    vippy = Vippy()
    vippy.run ()
