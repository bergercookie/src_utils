#!/usr/env/bin python

from math import factorial

sumn = 0
for n in range(3,10**6):
    string1 = str(n)
    sum1 = 0
    for i in string1:
        sum1 += factorial(int(i))
    if sum1 == n:
        print n
        sumn += n
print 'sum', sumn
