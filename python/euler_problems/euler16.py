#!/usr/bin/env python

"insert the number 2**1000 in a string"
a = str(2**1000)
"Iterate this string to find the sum of the numbers"
sum = 0
for i in a:
    sum += int(i)

print "sum of the digits", sum
