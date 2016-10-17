#!/usr/bin/env python

"How many different roots are to get from the upper left corner of a 20x20 grid to the down right corner?"
"Imports first"

import random
"from numpy import arange"
"list storing the different routes"
list1 = [ ]

for x in range(10**5):
    Rem0 = 20
    Rem1 = 20
    a=  [ ]
    "initialization of index"
    for i in range(40):
        if  Rem1 == 0:
            a = a + ['0']*Rem0  
            break
        elif Rem0 == 0:
            a = a + ['1']*Rem1
            break
        else:    
            choice = str(random.choice([0,1]))
            a.append(choice)
            if choice == 1: 
                Rem1 -= 1
            else: 
                Rem0 -= 1
    string1 =(''.join(a))
    list1.append(string1)
    print(string1)

Combinations = len(set(list1))
print "Number of Routes:\n", Combinations



