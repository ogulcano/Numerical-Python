import numpy as np
import matplotlib.pyplot as plt

def dydx(v):
    value = v
    return value
def dvdx(v,y,t):
    value = -v/t -(1-1/t)*y
    return value
t = 0.0001
h = 0.01
y0 = 1
v0 = 0
y = []
v = []
tv = []
while t < 30.1:
    y.append(y0)
    v.append(v0)
    tv.append(t)
    y0t = y0
    y0 += h*dydx(v0)
    v0 += h*dvdx(v0,y0t,t)
    t += h
y = np.array(y)
tv = np.array(tv)
plt.plot(tv,y,label = "Numerical")
plt.legend()
plt.show()
