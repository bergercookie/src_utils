#!/usr/bin/python

# Password Generation

# the  lenght is 5chars
# c1, c2, c3, c4, c5

# Possible values
# x, y, z

# Initialization
values = ['x', 'y', 'z']
pos_pass_list = []

for c1 in values:
    for c2 in values:
        for c3 in values:
            for c4 in values:
                for c5 in values:
                    pos_pass_list.append('%s%s%s%s%s\n'% (c1,c2,c3,c4,c5))

with open('pass1', 'w') as file1:
    for pos_pass in pos_pass_list:
        file1.write(pos_pass)

# Login Name
list_of_names = [\
        'jack' + '@PentesterAcademy.com',\
        'admin' + '@PentesterAcademy.com']
with open('login1', 'w') as file2:
    for name in list_of_names:
        file2.write(name + '\n')
