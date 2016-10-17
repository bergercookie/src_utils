#!/usr/bin/python

import re
import optparse

parser = optparse.OptionParser('usage %prog  <target_file>'+\
                               '-p <wordlist_file>')
parser.add_optin(-p, dest = 'wordlist', tpe='string', \
                    help='specify wordlist file')

with open(wordlist, 'r') as fd:
    for lines in fo:
        password = lines.split('\n')
        brute = subprocess.Popen(["./blackbuntu", "-f", "foo.txt", "-p", password[0]], stdout=subprocess.PIPE)
        if(re.search("Success", brute.communicate()[0])):
            print "Password Cracked and your Password is ", password[0]
            exit()
        else:
            print password[0], " is not Password"  
