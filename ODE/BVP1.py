#The problem => y''-y = 0; y(0) = 1, y'(1) = 0
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    c1 = 1/(1+np.exp(2))
    c2 = np.exp(2)/(1+np.exp(2))
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = c1*np.exp(x[i])+c2*np.exp(-x[i])
    return y
b1 = 0; b2 = 1; N = 50
h = (b2-b1)/N
M = np.zeros([N+1,N+1])
b = np.zeros(N+1)
xv = np.zeros(N+1)
for i in range(len(M)):
    for j in range(len(M)):
        if(i==0 and j==0):
            M[i,j] = 1
        elif(i==N and j==N):
            M[i,j] = 1
            M[i,j-2] = -1
        elif (i>0 and i< N and i==j):
            M[i,j] = -2-np.power(h,2)
            M[i,j-1] = 1
            M[i,j+1] = 1
    if i == 0:
        b[i] = 1
xs = np.linalg.solve(M,b)

x = np.linspace(b1,b2,N+1); y = f(x)
err = np.sum(np.abs(xs-y))/np.sum(np.abs(y))
print(f"The Error:{err*100:,.2f}%")
plt.plot(x,y,label="Exact Solution",color = "red",lw = 1)
plt.plot(x,xs,label="Numerical Solution",color = "blue",lw=1)
plt.legend()
plt.savefig("BVP1.png",dpi=300)
plt.show()