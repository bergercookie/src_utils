#!/usr/bin python

def sunarthsh(number):
    a = (number / 1000)
    b = (number / 100) % 10
    c = (number / 10) % 10
    d = (number % 10)
    list1 =  [a, b, c, d]
    return sum([x**4 for x in list1])

for number in range(1000, 10000):
    if number == sunarthsh(number): print number


