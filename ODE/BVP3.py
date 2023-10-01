#The problem => y''+y = 0; y(0)+y'(PI) = 0.75, 2*y'(0)+y(PI) = -1
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    c1 = 0.5
    c2 = -0.25
    y = np.zeros(len(x))
    for i in range(len(x)):
        y[i] = c1*np.cos(x[i])+c2*np.sin(x[i])
    return y
b1 = 0; b2 = np.pi; N = 1000
h = (b2-b1)/N
M = np.zeros([N+1,N+1])
b = np.zeros(N+1)
xv = np.zeros(N+1)
for i in range(len(M)):
    for j in range(len(M)):
        if(i==0 and j==0):
            M[i,j] = 2*h
            M[i,N] = 1
            M[i,N-2] = -1
        elif(i==N and j==N):
            M[i,j] = h
            M[i,0] = -1
            M[i,2] = 1
        elif (i>0 and i< N and i==j):
            M[i,j] = -2+np.power(h,2)
            M[i,j-1] = 1
            M[i,j+1] = 1
    if i == 0:
        b[i] = 1.5*h
    elif i == N:
        b[i] = -h
xs = np.linalg.solve(M,b)
x = np.linspace(b1,b2,N+1); y = f(x)
err = np.sum(np.abs(xs-y))/np.sum(np.abs(y))
print(f"The Error:{err*100:,.2f}%")
plt.plot(x,y,label="Exact Solution",color = "red",lw = 1)
plt.plot(x,xs,label="Numerical Solution",color = "blue",lw=1)
plt.legend()
plt.savefig("BVP3.png",dpi=300)
plt.show()