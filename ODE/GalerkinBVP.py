# The problem y"+2y=-x^2; y(0) = 0; y(1) = 0
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def E(x,n):
    return pow(x,n+1)-pow(x,n+2)
def LF(x,n):
    return (n+1)*n*pow(x,n-1)-(n+2)*(n+1)*pow(x,n)+ 2*(pow(x,n+1)-pow(x,n+2))
def F(x):
    return -pow(x,2)
N = 7; lw=0; ul=1
M = np.zeros([N,N])
b = np.zeros(N)
for i in range(N):
    for j in range(N):
        M[i,j] = quad(lambda x: E(x,i)*LF(x,j), lw, ul)[0]
    b[i] = quad(lambda x: E(x,i)*F(x), lw, ul)[0]
xs = np.linalg.solve(M,b)
x = np.linspace(lw,ul,10)
y = np.zeros(len(x))
for i in range(N):
    y +=xs[i]*E(x,i)
f1 = -0.5*np.cos(np.sqrt(2)*x) + (1/(2*np.tan(np.sqrt(2))))*np.sin(np.sqrt(2)*x) - 0.5*pow(x,2) + 0.5
plt.plot(x,y,label="Numerical",marker="*",lw=1)
plt.plot(x,f1,label = "Exact",lw=1)
plt.legend()
plt.savefig("GalerkinBVP.png",dpi=300)
plt.show()