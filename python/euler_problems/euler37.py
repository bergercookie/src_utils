#!/usr/bin/env python

from Sieve2 import erat14

def istrunctuated(number, primes):
    "function detects if a number is a trunc.prime"

    string1 = str(number)
    for j in range(1, len(string1)):
        if int( string1[j:]) not in primes: return False
        if int(string1[:len(string1)-j]) not in primes: return False

    return True


"first find all the prime numbers & create an array out of them"
primes1 = erat14(10**6)

"11 tructuable primes only"

sum1 = 0
for i in primes1[4:]:
    if istrunctuated(i,primes1) == True: 
        sum1 += i
        print i

print "the sum of all the trunctuated primes is", sum1

        

