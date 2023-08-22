import numpy as np
import matplotlib.pyplot as plt

def dydx(v):
    value = v
    return value
def dvdx(v,y,t):
    value = -t*y
    return value
t = 1
h = 0.01
y0 = 1
v0 = -1
y = []
v = []
tv = []
while t < 50.1:
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
