#!/usr/bin/env python
"reduce(lambda x , y: x*y, range(1,11)) -> factorial in one line using reduce"
def factorial(i):
    if i == 1:
        return 1
    else:
        return factorial(i-1)*i


number = input("Give me a positive number and I'll return its factorial")
fact = factorial(number)
mystring = str(fact)
sum1 = sum(int(i) for i in mystring)
print sum1

