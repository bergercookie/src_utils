#!/usr/bin/env python

import numpy as np
import scikits.bvp_solver as bvp_solver
import pylab

def rhs_function(x , y):
    return np.array([y[1] , 1-y[0]])




def boundary_conditions(ya,yb):
    return (np.array([ya[0] - 1]), np.array([yb[0]]))


# Implementing the ProblemDefinition technique

problem = bvp_solver.ProblemDefinition(num_ODE = 2,
                                               num_parameters = 0,
                                               num_left_boundary_conditions = 1,
                                               boundary_points = (0, np.pi),
                                               function = rhs_function,
                                               boundary_conditions = boundary_conditions)


# Solving the Bvp
solution = bvp_solver.solve(problem,
                            solution_guess = (2.0,
                                              2.0))

x = np.linspace(0, np.pi/2, 45)
y = solution(x)
print "Solution to the Boundary Value Problem", y

pylab.plot(x, y[0,:],'r-', ms = 2)
pylab.plot(x, y[1,:],'g.-', ms = 2)
pylab.legend('function 1', 'function # 2')
pylab.show()
