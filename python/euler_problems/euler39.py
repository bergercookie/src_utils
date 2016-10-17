#!/usr/env/bin python

def fun1(p):
    return lambda a,b,c: a+b+c == p & a**2 + b**2 == c*2 
