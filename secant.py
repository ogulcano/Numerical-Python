import matplotlib.pyplot as plt
import numpy as np

def secant(f,x1,x2,tol= 0.001,maxiter = 100):
    for iteration in range(maxiter):
        xnew  = x2 - (x2-x1)/(f(x2)-f(x1)) * f(x2)
        if abs(xnew-x2) < tol: break
        else:
            x1 = x2
            x2 = xnew
    else:
        print("Maximum number of iterations are reached!")
    return xnew, iteration

y = lambda x: np.cos(x) - np.abs(x)

x, n = secant(y,0,1)

print(x, n)