#!/usr/bin/env python

import itertools

print "The number of possible paths is",len(list(itertools.permutations([0]*20+[1]*20)))
