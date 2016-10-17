#!/usr/bin/env python

def ispalindrome(number):
    if type(number) == int:
        string1 = str(number)
        for i in range(1,(len(string1)/2)+1):
            if string1[i-1] != string1[-i]: return False
    else:
        for i in range(1,(len(number)/2)+1):
            if number[i-1] != number[-i]: return False
    return True
        
    
sum1 = 0
for i in range(1,10**6):
    if ispalindrome(i) and ispalindrome(bin(i).lstrip('0b')):
        sum1 += i

print"The summary of all the palindrome( in both bases) numbers is", sum1
