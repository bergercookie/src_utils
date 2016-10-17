#!/usr/bin/python

content = open('passes', 'w')

for i in range(10):
    for j in range(10):
        for k in range(10):
            content.write('%s%s%s' %(i, j, k) + '\n')
