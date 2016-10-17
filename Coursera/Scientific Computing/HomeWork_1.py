#!usr/bin/env python

#Imports
from numpy import array, sqrt, linspace
from scipy.integrate import odeint
from matplotlib.pyplot import plot, show, hold

#I first define the psi array as a function.
def func1(psi, x):
    return array([psi[1],(x**2 - epsilon)*psi[0]]) # f(x) for psi[0], psi[1]

#Initial Conditions

psi0_start = 1 # Arbitrarily, Linear ODE
def ic(epsilon, psi0_start, L): # pass in  epsilon, psi0_start, return array with psi0_start, psi0_end
    return array([psi0_start, sqrt(abs(L**2 - epsilon*psi0_start))])

#Definition of x vector [start, end, step]

xspan = linspace(-4, 4 ,1000)
hold(True)

tol = 10**(-4)
#first_approx = 100
epsilon = input('Give Epsilon: ')
L = input('Give the limit L: ')
#for j in range(1000):
#depsilon = 1
sol = odeint(func1, ic(epsilon, psi0_start, L), xspan)
#Check the second equation

end_approxim = sol[-1, 1] + sqrt(abs(16 - epsilon*sol[-1, 0]))    # !abs?
#if end_approxim
#    epsilon += depsilon
#else


if __name__ == '__main__':
    plot(xspan, sol[:,0])
    show()
    print 'for epsilon = ',epsilon,':\n','Ending Equation Tolerance', end_approxim
