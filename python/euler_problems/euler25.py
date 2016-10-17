#!/usr/bin/env python


def Fibonacci(term, fib1, fib2):
    "fib1, fib2 previous fib number and 2nd previous fib number"

    """   if term == 1 or term ==2: 
           return 1 """
    Fibonacci= fib1 + fib2
    fib2 = fib1
    fib1 = Fibonacci
    print Fibonacci
    return Fibonacci, fib1, fib2
    



"Fibonacci(term) is the value of the term"
"flag = False"
prev1 = prev2 = 1

for i in range(1, 10**5):
    "print i"
    (a, prev1, prev2) = Fibonacci(i, prev1, prev2)
    print a
    "print prev1 ,prev2"
    if len(str(a)) == 1000:
        print"The ",i+2,"th term of the Fibonacci sequence is the first that has 1000 digits\n",i+2 
        "flag = True"
        print(a)
        break

