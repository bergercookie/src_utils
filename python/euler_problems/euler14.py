#!/usr/bin/env python

#Project Euler
#Project 14(Non-optimised solution, takes a few minutes to find answer)

i=1
terms={}
for i in range(1,10**6+1):
   counts=2    #one for each of the starting and finishing values
   n=i
   while n!=1:
      if n%2==0:
         n=n/2
      else:
         n=3*n+1
      counts+=1

   terms[counts]=i

print(terms[max(terms)])



