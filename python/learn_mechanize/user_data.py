#!/usr/bin/env python

from __future__ import print_function
import random


# Import last names
with open('last_names.txt') as fd_last:
    lnames = fd_last.readlines()
    lnames = [lname.rstrip().capitalize() for lname in lnames] #remove \n, capitalize
# Import first names
with open('first_names.txt') as fd_first:
    fnames = fd_first.readlines()
    fnames = [fname.rstrip().capitalize() for fname in fnames] #remove \n, capitalize
fnames = fnames[5:] # remove first comments

nUsers = 100;

# making an initial selection
selection = [random.randint(0, len(lnames)) for i in range(nUsers)]
names_f = [lnames[i] for i in selection]

#print('Set filtered.\nlen = %d\nlnames_f = %s' %(len(names_f), names_f))

# adding the first name
for i in range(len(names_f)):
    first = fnames[random.randint(0, len(fnames)-1)]
    names_f[i] = '{0} {1}'.format(first, names_f[i])

#print('Added first names.\nlen = %d\nlnames_f = %s' %(len(names_f), names_f))


