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
# Initial Value
t = 0  
y = 1
h = 0.1
while t < 4.1:
    yt = 0
    yv.append(y)
    tv.append(t)
    m = df(t,y)
    y += 0.5*h*(df(t,y)+df(t+h,y+m*h))
    t += h 
yv = np.array(yv)
tv = np.array(tv)
av = np.array(u(tv,1))
error = (av-yv)/yv * 100
print("True values:{}\nApproximated Values:{}\nErrors:{}".format(av,yv,error))
plt.plot(tv,yv,"*",label= "Numerical",color = "red")
plt.plot(tv,av,label = "Analytical",color = "black")
plt.legend()
plt.show()