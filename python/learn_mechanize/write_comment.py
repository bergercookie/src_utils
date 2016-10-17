#!/usr/bin/env python

from __future__ import print_function
import mechanize
import sys

br = mechanize.Browser()

# aditional configuration parameters
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this


url = 'http://se.mathworks.com/matlabcentral/answers/1427-what-' +\
        'frustrates-you-about-matlab'

# make the connection
response = br.open(url)


