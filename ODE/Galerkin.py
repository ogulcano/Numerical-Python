# The problem u"(x) = lambda*x; u(0) = 0, u(1) = 0
import numpy as np
import matplotlib.pyplot as plt
def element(x,n):
    p = pow(x,n+1)-pow(x,n+2)
    return p
def iM(m,n,a,b):
    p1 = ((n*(n+1)))*(pow(b,m+n+1)-pow(a,m+n+1))/(m+n+1)
    p2 = ((2*(n+1)*(n+1)))*(pow(b,m+n+2)-pow(a,m+n+2))/(m+n+2)
    p3 = (((n+2)*(n+1)))*(pow(b,m+n+3)-pow(a,m+n+3))/(m+n+3)
    return p1 - p2 + p3
def ib(m,a,b):
    p1 = (pow(b,m+3)/(m+3)-pow(a,m+3))/(m+3)
    p2 = (pow(b,m+4)-pow(a,m+4))/(m+4)
    return p1 - p2
N = 20
M = np.zeros([N,N])
b = np.zeros(N)
xs = np.zeros(N)
lamd = 1
for i in range(N):
    for j in range(N):
        M[i,j] = iM(i,j,1,0)

    b[i] = lamd*ib(i,1,0)
print(M)
print(b)
xs = np.linalg.solve(M,b)
print(xs)
x = np.linspace(0,1,10)
y = np.zeros(len(x))
f = np.zeros(len(x))
for i in range(len(x)):
    value = 0
    for j in range(N):
        value +=xs[j]*element(x[i],j)
    y[i] = value
    f[i] = (lamd/6)*pow(x[i],3) + (-lamd/6)*x[i]
plt.plot(x,y,label="Galerkin",marker="o",lw=1)
plt.plot(x,f,label="Exact",lw=2)
plt.legend()
plt.savefig("Galerkin.png",dpi=300)
plt.show()
