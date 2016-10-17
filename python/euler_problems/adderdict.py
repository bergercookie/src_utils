#!/usr/bin/env python

def addDict(dict1 ,dict2):
    """
    Computes the union of two dictionaries
    """
    final_dict = {}
    for (i,j) in dict1.items():
        final_dict[i] = j
    for (i,j) in dict2.items():
        final_dict[i] = j
    return final_dict

