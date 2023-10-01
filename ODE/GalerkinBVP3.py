# The problem y"+3y'+2y=10*e^(-2x); y(0) = 0; y(1) = 1
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
def E(x,n):
    return pow(x,n+2)
def LF(x,n):
    return (n+2)*(n+1)*np.power(x,n)+3*(n+2)*np.power(x,n+1)+2*np.power(x,n+2)
def F(x):
    return 10*np.exp(-2*x)
N = 9; lw=0; ul=1
M = np.zeros([N,N])
b = np.zeros(N)
for i in range(N):
    for j in range(N):
        M[i,j] = quad(lambda x: E(x,i)*LF(x,j), lw, ul)[0]
    b[i] = quad(lambda x: E(x,i)*F(x), lw, ul)[0]
xs = np.linalg.solve(M,b)
x = np.linspace(lw,ul,20)
y = np.zeros(len(x))
for i in range(N):
    y +=xs[i]*E(x,i)
c1 = (1+10*np.exp(-2))/(np.exp(-1)-np.exp(-2))
c2 = -c1
f1 = c1*np.exp(-x)+c2*np.exp(-2*x)-10*x*np.exp(-2*x)
plt.plot(x,y,label="Numerical",marker="*",lw=1)
plt.plot(x,f1,label = "Exact",lw=1)
plt.legend()
plt.savefig("GalerkinBVP3.png",dpi=300)
plt.show()