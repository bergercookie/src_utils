#!/usr/bin/python
# Sat Sep 20 17:54:01 EEST 2014, nickkouk

import urllib2
import re

# Varius Definitions
site_url = 'http://www.passworddragon.com/avoid-common-passwords'

# Determine password list
content = urllib2.urlopen(site_url).read()
print "Downloaded Content"

extracted = re.findall(r'<li>.*</li>',  content)
passwords = [i[4:-5] for i in extracted]

print "Passwords Extracted"
# Pass passwords to file
my_file = open('passes_2', 'w')
for one_pass in passwords:
    my_file.write('%s\n' % one_pass)

my_file.close()
