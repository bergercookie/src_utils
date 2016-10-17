#!/usr/bin/python
# Sat Sep 20 17:54:01 EEST 2014, nickkouk

import urllib2
import re

# Varius Definitions
site_url = 'http://www.passworddragon.com/avoid-common-passwords'

# Determine password list
content = urllib2.urlopen(site_url).read()

extracted = re.findall(r'<li>.*</li>',  content)
passwords = [i[4:-5] for i in extracted[2:-1]]
classics = ['root', 'admin', 'administrator']
passwords_combined = passwords + classics

# Pass passwords to file
my_file = open('passes_4', 'w')
for one_pass in passwords_combined:
    for number in range(10):
        my_file.write('%s%s\n' % (one_pass, number))

my_file.close()
