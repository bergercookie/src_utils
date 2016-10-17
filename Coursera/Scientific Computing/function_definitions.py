from numpy import exp, cos, sin
def df(x):
    #returns the derivative of the function at the x-point
    return exp(x) - cos(x)
    
def f(x):
    #return the value of the function at the x-point
    return exp(x) - sin(x)
    
def Newton_Method(x0):
    return x0 - float(f(x0))/df(x0) # x1
        
tol = 0.001
x_init = x0 = -3
x1 = Newton_Method(x0)
   
while abs(x1 - x0) > tol:
    x0 = x1
    x1 = Newton_Method(x1)
if __name__ == "__main__":
    Solution = x1 
    print "for the starting guess", x_init," and desired tolerance", tol, " the approximate solution is", Solution
    