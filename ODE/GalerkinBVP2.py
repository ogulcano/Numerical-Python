# The problem y"+a*y=-x; y(0) = 0; y(1) = 0
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def E(x,n):
    return pow(x,n+1)-pow(x,n+2)

def LF(x,n,a):
    return (n+1)*n*pow(x,n-1)-(n+2)*(n+1)*pow(x,n)+ a*(pow(x,n+1)-pow(x,n+2))

def F(x):
    return -x
a = 1 # Define the parameter a
E1 = 2; E2 = 8
for N in range(E1,E2):
    lw=0; ul=1
    M = np.zeros([N,N])
    b = np.zeros(N)
    for i in range(N):
        for j in range(N):
            M[i,j] = quad(lambda x: E(x,i)*LF(x,j,a), lw, ul)[0]
        b[i] = quad(lambda x: E(x,i)*F(x), lw, ul)[0]
    xs = np.linalg.solve(M,b)
    x = np.linspace(lw-2,ul+1,25)
    y = np.zeros(len(x))
    for i in range(N):
        y +=xs[i]*E(x,i)
    f1 = ((1/(a*np.sin(np.sqrt(a)))))*np.sin(np.sqrt(a)*x) - x/a
    if N == E1:
        plt.plot(x,f1,label = "Exact",lw=3)
    plt.plot(x,y,label= f"Numerical:{N}",marker="*",lw=1)

    plt.legend()
    plt.savefig("GalerkinBVP2.png",dpi=300)
plt.show()