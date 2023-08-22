import numpy as np
import matplotlib.pyplot as plt
def u(t): # Analytical Solution
    value = 1 + 0.5 * np.exp(-4*t) + (-0.067667641)* np.exp(-2*t)
    return value
def df(t,y):
    value = 2 - np.exp(-4*t) - 2*y
    return value
yv = []
tv = []
# Initial Value
t = 1  
y = 1 
h = 0.05
while t < 3.1:
    yv.append(y)
    tv.append(t)
    m = df(t,y)
    t += h
    y += h*m
yv = np.array(yv)
tv = np.array(tv)
av = np.array(u(tv))
error = (av-yv)/yv * 100
print("True values:{}\nApproximated Values:{}\nErrors:{}".format(av,yv,error))
plt.plot(tv,yv,"*",label= "Numerical",color = "red")
plt.plot(tv,av,label = "Analytical",color = "black")
plt.legend()
plt.show()