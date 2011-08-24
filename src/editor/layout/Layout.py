'''
Created on Aug 21, 2011

@author: shaun
'''

import abc
from abc import ABCMeta

class Layout(metaclass=ABCMeta):

    @abc.abstractmethod
    def __init__(self):
        pass
    
    
        