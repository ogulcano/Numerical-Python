import numpy as np
import matplotlib.pyplot as plt
def u(t,c):
    value = np.sqrt(2*t + c)
    return value
def df(t,y):
    value = 1/y
    return value
yv = []
tv = []
t = 0
y = 1
c = y**2
h = 0.05
while t < 1.1:
    yv.append(y)
    tv.append(t)
    m = df(t,y)
    t += h
    y += h*m
yv = np.array(yv)
tv = np.array(tv)
av = np.array(u(tv,c))
error = np.abs(av-yv)/yv * 100
print("True values:{}\nApproximated Values:{}\nErrors:{}".format(av,yv,error))
plt.plot(tv,yv,label= "Numerical",color = "red")
plt.plot(tv,av,label = "Analytical",color = "black")
plt.legend()
plt.show()