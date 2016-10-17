#!/usr/bin/env python

# Euler 9
# Nikos Koukis <nickkouk@gmail.com>
# Vangelis Koukis <vkoukis@gmail.com>

for a in range(1,1000):
    for b in range(a, 1000):
        if 1000**2 - 2000*(a+b)+2*a*b == 0:
            print "Brhka a=", a, "b=", b, "c=", 1000-a-b
            print "Product: ", a*b*(1000-a-b)

# One-line solution
# (bruteforce)
filter(lambda z: 1000000-2000*(z[0]+z[1])+2*z[0]*z[1]==0,[(x,y) for x in range1000 for y in range1000])
