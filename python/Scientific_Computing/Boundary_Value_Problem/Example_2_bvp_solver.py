#!/usr/bin/env python

import scikits.bvp_solver
import pylab
import numpy as np

print "Test 1"

def rhs_function(X, Y):
    return np.array([Y[1], -(X*Y[0]-1.0)*Y[0]])

def dfunction(X, Y):
    PD = np.zeros((2,2))
    PD[0, 1] = 1.0
    PD[1, 0] = 1. - 2*X*Y[0]
    return PD



def boundary_conditions1(YA,YB):
    BCA = np.zeros(1)
    BCB = np.zeros(1)
    BCA[0]=YA[1]
    BCB[0]=YB[0]+YB[1]
    return BCA,BCB

def guess_y1(X):
    Y = np.zeros(2)
    if X <= 1.5:
        Y[0] = 2
        Y[1] = 0
    else:
        Y[0] = 2.*np.exp(1.5 - X)
        Y[1] = -Y[0]
    return Y

singular_term = np.zeros((2,2))
singular_term[1,1] = -4.

L= [5, 8, 10, 20]
solutionList = [ ]
problemList = [ ]

for i in range(4):
    problemList.append(scikits.bvp_solver.ProblemDefinition(num_ODE=2,
                                                            num_parameters=0,
                                                            num_left_boundary_conditions=1,
                                                            boundary_points=(0,L[i]),
                                                            function = rhs_function,
                                                            boundary_conditions=boundary_conditions1,
                                                            function_derivative = dfunction))

    if i == 0:
        solutionList.append(scikits.bvp_solver.solve(problemList[i],
                                                     solution_guess = guess_y1,
                                                     singular_term = singular_term,
                                                     max_subintervals = 300))
    else:
        solutionList.append(solutionList[i-1].extend(0,L[i]))
        solutionList[i]=scikits.bvp_solver.solve(problemList[i],
                                                 solution_guess=solutionList[i],
                                                 singular_term=singular_term,
                                                 max_subintervals=300)

for i in range(4):
    x=np.linspace(problemList[i].boundary_points[0],problemList[i].boundary_points[1],45)
    y=solutionList[i](x)

    #Plotting the results

    pylab.subplot(1,4,i+1)
    pylab.plot(x,y[0,:],'-')
    pylab.plot(x,y[1,:],'-')

pylab.show()

