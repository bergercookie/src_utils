#!/usr/bin/env python

def step1(step, ind): return ind + step
def step2(step, ind): return ind + step + 1


# import the numbers given in a list of sublists
list1 =[i.rstrip().split() for i in open('input18').readlines()]

#strings to integers in list1
for i in range(15):
    for j in range(len(list1[i])):
        list1[i][j] = int(list1[i][j])



