#!/usr/bin/env python
# Fri Aug 1 12:21:30 EEST 2014, nickkouk

# Imports first
import numpy as np
import optparse
import supplement as sp

# Matrix initialization
list_rows = [ ]
row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',\
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

list_rows.append(row)
for i in range(1, 26):
    list_rows.append(list_rows[i-1][1:] + list(list_rows[i-1][0]))

list_rows = np.array(list_rows)


