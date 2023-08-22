import matplotlib.pyplot as plt
import numpy as np

def nraphson(fn,x,tol = 0.001,maxiter = 100):
    for i in range(maxiter):
        xnew = x - fn[0](x)/fn[1](x)
        if abs(xnew - x) < tol: break
        x = xnew
    return xnew, i
y = [lambda x: np.cos(x) - x,lambda x: -np.sin(x) - 1]
x, n = nraphson(y,1)
print(f"The root: {x}\nIterations:{n}")

