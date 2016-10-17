#!/usr/bin/python

# Imports
from euler_functions import pr_divisors, is_abundant, abundant_until_n
from itertools import permutations

# Declarations
my_sum = 0
limit = 28123

abundants = (x for x in range(12, limit + 1) if is_abundant(x))
dif_perms = permutations(abundants)
(i+j for (i,j) in dif_perms)

        


print "***Sum of integers that cannot be writtent " +\
        "as the sum of two abundant numbers***"
print sum(range(1, limit + 1)) - my_sum

    
