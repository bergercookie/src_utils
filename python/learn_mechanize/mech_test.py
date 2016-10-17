#!/usr/bin/env python

# using mechanize, Mathworks.com


# Imports first
from __future__ import print_function
import mechanize
from time import sleep
import sys

site_link = 'http://se.mathworks.com/matlabcentral'

br = mechanize.Browser()

# aditional configuration parameters
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this


# make the connection
response = br.open(site_link)
#print response.read()


# find the login #
##################

login_url = ''
print("Searching through available links", end = '')
for link in br.links():
    print('.', end=''); sys.stdout.flush()
    if 'Log In' in link.text:
        # found the logging link!
        login_link = link
        print('\nLogin link Found!')
        break

if not login_link: # link not found
    raise Exception('Login link not found')
else: # go to login
    request = br.follow_link(login_link)
    print("Entering Login page..")

print('Forgot your password in page: [%s]' %('Forgot your password?' in \
        br.response().read()))

# Login Screen #
################

br.select_form("loginFormAccess") 
mail = 'nkoukis@kth.se'
passwd = 'Kalimera_matlab12!'

# find the needed controls
user_c = br.form.find_control('userId');
pass_c = br.form.find_control('password')

# fill in the values
user_c.value = mail
pass_c.value = passwd

response = br.submit()
print(response.read())
