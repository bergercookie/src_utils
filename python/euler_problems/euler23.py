#!/usr/env/bin python

def is_abundant(n):
    """Find  if a number is abundant."""
    return sum(filter(lambda i: n % i == 0, range(1, n / 2 + 1))) > n

# table is initialized as range(1,28123) and the I pop out all the non - eligible numbers
table = range(1,28123)
abundants =filter(is_abundant, range(1,28123))
print 'ok abundants'

def colla(n):
    """ Find all the collaborations of n with all the other abundant numbers ( > n)"""
    for i in abundants[abundants.index(n):]:
        try:
            table.remove(i+n)
        except:
            pass
for n in abundants:
    colla(n)
# The sum of the eligible numbers is needed
print(sum(table))
