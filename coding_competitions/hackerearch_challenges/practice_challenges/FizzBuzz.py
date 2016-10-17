#!/usr/bin/python

# Basic Inputs
no_tests = input()
numbers = [int(i) for i in raw_input().split()] # Do not use ' ' !!!

for number in numbers:
    for counter in range(1, number+1):
        if counter % 3 == 0 and counter % 5 == 0:
            print "FizzBuzz"
        elif counter % 3 == 0:
            print "Fizz"
        elif counter % 5 == 0:
            print "Buzz"
        else:
            print counter
