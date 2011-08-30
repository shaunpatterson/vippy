'''
Created on Aug 30, 2011

Various formatting functions.  

@author: Shaun Patterson
'''

import logging
from textwrap import TextWrapper

logger = logging.getLogger (__name__)

def wordWrap (lines, rows, cols):
    ''' Format an array of text to a specific number of 
        visible rows and columns '''
    wrapped = []

    # Set up a TextWrapper
    wrapper = TextWrapper ()
    wrapper.width = cols
    wrapper.expand_tabs = False
    wrapper.replace_whitespace = False
    wrapper.drop_whitespace = False
    
    for line in lines:
        if len (line) > cols:
            wrapped.extend (wrapper.wrap (line))
        else:
            wrapped.append (line)
            
        if len (wrapped) >= rows:
            break
       
    # Return only "rows" in case a word wrap added extra
    return wrapped [:rows] 
        
    
    
        