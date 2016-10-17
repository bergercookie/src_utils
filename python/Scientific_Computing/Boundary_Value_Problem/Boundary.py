#!/usr/bin/env python

import numpy as np
import scikits.bvp_solver as bvp_solver
import pylab
T10 = 130
T2Ahx = 70
Ahx = 5
U = 1.0

def rhs_function(a , T):
    q = (T[0] - T[1]) * U
    return np.array([-q , q/-2.0])




def boundary_conditions(Ta,Tb):
    return (np.array([Ta[0] - T10]), np.array([Tb[1] - T2Ahx]))


# Implementing the ProblemDefinition technique

problem = bvp_solver.ProblemDefinition(num_ODE = 2,
                                               num_parameters = 0,
                                               num_left_boundary_conditions = 1,
                                               boundary_points = (0, Ahx),
                                               function = rhs_function,
                                               boundary_conditions = boundary_conditions)


# Solving the Bvp
solution = bvp_solver.solve(problem,
                            solution_guess = ((T10 + T2Ahx)/2.0,
                                              (T10 + T2Ahx)/2.0))

A = np.linspace(0, Ahx, 45)
T = solution(A)
print "Solution to the Boundary Value Problem", T

pylab.plot(A, T[0,:],'r-', ms = 2)
pylab.plot(A, T[1,:],'g.-', ms = 2)
pylab.legend('function 1', 'function # 2')
pylab.show()
