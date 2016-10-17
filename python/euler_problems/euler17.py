#!/usr/bin/env python 

def monades(number):
    if number == '0': return ''
    elif number == '1': return 'one'
    elif number == '2': return 'two'
    elif number == '3': return 'three'
    elif number == '4': return 'four'
    elif number == '5': return 'five'
    elif number == '6': return 'six'
    elif number == '7': return 'seven'
    elif number == '8': return 'eight'
    elif number == '9': return 'nine'

def dekades(number):
    if number == '2': return 'twenty'
    elif number == '3': return 'thirty'
    elif number == '4': return 'forty'
    elif number == '5': return 'fifty'
    elif number == '6': return 'sixty'
    elif number == '7': return 'seventy'
    elif number == '8': return 'eighty'
    elif number == '9': return 'ninety'

def apo10_20(number):
    if number == '1': return 'eleven'
    elif number == '2': return 'twelve'
    elif number == '3': return 'thirteen'
    elif number == '4': return 'fourteen'
    elif number == '5': return 'fifteen'
    elif number == '6': return 'sixteen'
    elif number == '7': return 'seventeen'
    elif number == '8': return 'eighteen'
    elif number == '9': return 'nineteen'

first_list = [str(i) for i in range(1,100)]

for i in range(1, 10):
    first_list[i - 1] = monades(first_list[i - 1])

for i in  range(20,100):
    try:
        first_list[i - 1] = dekades(first_list[i - 1][0]) + monades(first_list[i - 1][-1])
    except:
        print first_list[i]

for i in range(11, 20):
    first_list[i - 1] = apo10_20(str(first_list[i-1][-1]))

first_list[9] = 'ten'

letter_sum = 0
for i in first_list:
    for j in i:
        letter_sum += 1
# this is the sum of the letters in (1 - 99)
print 'letters1_99', letter_sum

# list for storing the letters of the first 9 digits
# letters of '1' in index 1
firstletters = [0]
for i in range(1, 10):
    sum1 = 0
    for j in monades(str(i)): sum1 += 1
    firstletters.append(sum1)

letters1_99  = letter_sum
# letters in 100 - 999
for i in range(1,10):
    letter_sum += letters1_99 * (7 + 3 + firstletters[i])

# for 100, 200, 300, 400...
for i in range(1,10):
    letter_sum += (7 + firstletters[i])
# for 1000
letter_sum += 11

print letter_sum, 'for all the numbers up to 1000'
