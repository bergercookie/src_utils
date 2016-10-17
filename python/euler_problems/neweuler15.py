#!/usr/bin/env python

def listplus0(list1):
    return [i+'0' for i in list1]


def listplus1(list1):
    return [i+'1' for i in list1]

"CANNOT use random"

"list for storing combinations"
Combinations = ['0']
"every item in the list must have 40 digits"
while len(Combinations[0])<40:
    
    Combinations = listplus0(Combinations) + listplus1(Combinations)

print "Number of Combinations", len(Combinations)


