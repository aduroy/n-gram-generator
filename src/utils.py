'''
Created on 8 nov. 2015

@author: Antonin Duroy
'''

def get_none_tuple(size):
    """ Create a tuple filled with None values
    """
    t = ()
    for i in range(size):
        t += (None,)
    return t

def get_none_list(size):
    """ Create a list filled with None values
    """
    l = [None]
    return l*size