#!/usr/bin/env python
#Euler No8

f=open('string','r')
mystring=f.read()
mystring=mystring.replace('\n','1')
pr=[]
for i in range (0,1000): 
    pr.append(int(mystring[i])*int(mystring[i+1])* 
            int(mystring[i+2])*int(mystring[i+3])*int(mystring[i+4]))
print max(pr)
