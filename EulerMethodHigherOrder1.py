import numpy as np
import matplotlib.pyplot as plt

def dydx(v):
    value = v
    return value
def dvdx(v,y):
    value = -3*v-2*y
    return value
def f(t):
    value = 2*np.exp(-t) - np.exp(-2*t)
    return value
t = 0
h = 0.1
y0 = 1
v0 = 0
y = []
v = []
tv = []
while t < 10.1:
    y.append(y0)
    v.append(v0)
    tv.append(t)
    y0t = y0
    y0 += h*dydx(v0)
    v0 += h*dvdx(v0,y0t)
    t += h
print(tv.index(0.5),y[tv.index(0.5)])
y = np.array(y)
tv = np.array(tv)
plt.plot(tv,y,label = "Numerical")
plt.plot(tv,f(tv),label = "Exact")
plt.legend()
plt.show()
