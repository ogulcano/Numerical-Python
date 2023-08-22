import numpy as np
def rfalsi(f,x1,x2,tol = 1.0e-06,maxfpos = 100):
    xh = 0
    fpos = 0
    if f(x1)*f(x2) < 0:
        for fpos in range(1,maxfpos+1):
            xh = x2 - (x2 - x1)/(f(x2)-f(x1)) * f(x2)
            if abs(f(xh)) < tol: break
            elif f(x1)*f(xh) < 0:
                x2 = xh
            else:
                x1 = xh
    else:
        print("No roots exist!")
    return xh, fpos

y = lambda x: np.cos(x) - np.abs(x)

x, n = rfalsi(y,0,1)
print(x,n)