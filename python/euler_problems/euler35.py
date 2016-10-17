#!/usr/env/bin python

"module for primes until n"
from Sieve2 import erat14
primes = erat14(10**6)

from itertools import permutations

def is_circular(sublist):
    "list1 is an int list, sublist is a list of strings "
    for i in sublist:
        if int(i) not in primes: return False
#    print i
    return True

Circulars = 0

for n in range (1, 10**6):
    all_of_them = [''.join(i) for i in list(permutations(list(str(n))))]
    if is_circular(all_of_them) == True: 
        Circulars +=1 
        print n
print 'number of circular numbers:', Circulars

