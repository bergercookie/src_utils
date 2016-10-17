#!/usr/bin/env python

# Sat May 17 10:56:28 EEST 2014, nickkouk

"""
***DOCUMENTATION***
The purpose of this programme is to calculate all the geometric elements of the
construction with regards to the x vertical distance of the B point
"""

from __future__ import division # python 2 stuff
import numpy as np
import sympy as sm
from scipy.optimize import newton

# constant declarations
from numpy import pi
init_lenght = 2.40

x = input('Give the x distance: ')
while x >= 2.5 or x < 1:
    x = input('x must be inside a certain range:\n')

L = lambda x: np.sqrt(x ** 2 - 2 * init_lenght * x + (init_lenght ** 2 + 5 ** 2))
a = lambda z: np.sqrt( (init_lenght - 1.8 - z) ** 2 + 1)
z_sol = newton(lambda z: (1.8 + z - x) ** 2 + 4 ** 2 - (L(x) - a(z)) ** 2  ,0.5)
theta = np.arctan((init_lenght - x) / 5.)
ver_target = np.tan(theta) * 1.5 + x

side_stick = (19 * np.tan(theta) + 30) / 2

print "*** Geometrical Dimensions ***"
print "x = {0} m\nL = {1} m\nz = {2} m\ntheta = {3} deg".format(np.round(x, 3), np.round(L(x), 3), np.round(z_sol, 3), np.round(theta * 180 / pi, 3)) 
print "Rope lenght until obstacle: {} m".format(np.round(a(z_sol), 3))
print "Target vertical position: {} m".format(ver_target)

print "\n*** Telepherique Dimensions ***"
print "Side stick lenght: {} cm".format(side_stick)    
