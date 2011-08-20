'''
Created on Aug 15, 2011

@author: shaun
'''

import logging.config
from threading import Thread

logging.config.fileConfig('logging.conf')
logger = logging.getLogger (__name__)


class Vippy (Thread):
    
    def __init__ (self):
        Thread.__init__(self)
    
    def run (self):
        logger.debug ("Vippy has started")
        
    

if __name__ == '__main__':
    vippy = Vippy()
    vippy.start ()
