#!/usr/bin/env python

"""function for finding the proper divisors and returning their sum"""

def d(number):
    sum1 = 0
    for i in range(1,number/2+1):
        if number%i == False: sum1 +=i
    return sum1

AmSum = 0 #sum of all the amicable numbers, Initialization

Amlist = [ ]
"list1 = [d(i) for i in range(1,10000)]"
for a in range(1,10000):
    b = d(a)
    if b < 10000:
        if d(b) == a:
            if a != b:
                Amlist.append(a)

print "sum of list",sum(Amlist)
print Amlist
Amset = set(Amlist)
print'lenght of Set',(len(Amset))
