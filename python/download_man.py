#!/usr/bin/env python

# Fri Apr 24 11:51:26 CEST 2015, nickkouk
# This is an experimental script to raise the downlaods of my first matlab file
# in FileExchange. 

import urllib2
import time

link = 'https://www.mathworks.com/matlabcentral/fileexchange/submissions/50613/v/1/download/zip'
times2run = 5000;

for i in range(1, times2run+1):
    urllib2.urlopen(link)
    print('Downloaded it %d times.' %i)
    #time.sleep(5);

    ange
    URL


