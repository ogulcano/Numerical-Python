import numpy as np
import matplotlib.pyplot as plt

def dydx(v):
    value = v
    return value
def dvdx(w):
    value = w
    return value
def dwdx(w,v,y):
    value = 5*w + 22*v - 56*y
    return value
def f(t):
    value = (14/33)*np.exp(-4*t) + (13/15)*np.exp(2*t) - (16/55)*np.exp(7*t)
    return value
t = 0
h = 0.001
y0 = 1
v0 = -2
w0 = -4
y = []
v = []
tv = []
while t < 1.1:
    y.append(y0)
    v.append(v0)
    tv.append(t)
    y0t = y0
    v0t = v0
    y0 += h*dydx(v0)
    v0 += h*dvdx(w0)
    w0 += h*dwdx(w0,v0t,y0t)
    t += h
y = np.array(y)
tv = np.array(tv)
plt.plot(tv,y,label = "Numerical")
plt.plot(tv,f(tv),label = "Exact")
plt.legend()
plt.show()
