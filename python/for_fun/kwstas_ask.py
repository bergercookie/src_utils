#!/usr/bin/env python

# imports
import argparse, sys

# parsing the input arguements
parser = argparse.ArguementParser('Children information')
parser.add_arguement('--children', dest = 'num_children', help='number of children in the area')


args = parser.parse_args()
