import matplotlib.pyplot as plt
import numpy as np
x = [0,10,20,30,40,50]
y = [26.0,32.4,37.2,48.6,52.8,55.3]

xplt = np.linspace(x[0],x[-1])
yplt = np.array([],float)
m = len(x)
n = m - 1
v = []
for xp in xplt:
    yp = 0
    for i in range(n+1):
        p = 1
        for j in range(n+1):
            if j != i:
                p *= (xp-x[j])/(x[i]-x[j])
        yp +=y[i]*p
    yplt = np.append(yplt,yp)

plt.plot(x,y,'ro',xplt,yplt,'b-')
plt.xlabel("x")
plt.ylabel("y")
plt.show()