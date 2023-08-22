import numpy as np
import matplotlib.pyplot as plt
xv = []
yv = []
xu = []
yu = []
x, y= 0, 0
for i in range(1000):
    alpha = np.random.random()
    r = 2*np.random.random()
    xv.append(r*np.cos(alpha*2*np.pi) + x)
    yv.append(r*np.sin(alpha*2*np.pi) + y)
    r = np.random.randint(3)
    xu.append(r*np.cos(alpha*2*np.pi) + x)
    yu.append(r*np.sin(alpha*2*np.pi) + y)
plt.figure(figsize=(5,5),dpi= 100)
plt.scatter(xv,yv,color = "blue")
plt.scatter(xu,yu,3, color = "red")
plt.show()
