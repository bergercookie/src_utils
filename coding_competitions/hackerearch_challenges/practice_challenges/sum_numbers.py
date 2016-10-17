#!/usr/bin/python

no_tests = input()
for glob_counter in range(no_tests):
    number_list = [int(i) for i in raw_input().split(' ')]
    print sum(number_list)


