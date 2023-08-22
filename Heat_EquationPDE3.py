import numpy as np
import matplotlib.pyplot as plt
# Crank Nicholson Method
h = 0.05
k = 0.025
x = np.arange(0,1+h,h)
t = np.arange(0,0.1+k,k).round(3)

boundaryConditions = [0,0]
initialConditions = np.sin(np.pi*x)

n = len(x)
m = len(t)
T = np.zeros((n,m))

T[0,:] = boundaryConditions[0]
T[-1,:] = boundaryConditions[1]
T[:,0] = initialConditions
factor = k/h**2
A = np.diag([2+2*factor]*(n-2),0) + np.diag([-factor]*(n-3),-1) + np.diag([-factor]*(n-3),1)
B = np.diag([2-2*factor]*(n-2),0) + np.diag([factor]*(n-3),-1) + np.diag([factor]*(n-3),1)

for j in range(0,m-1):
    b = T[1:-1,j].copy()
    b = np.dot(B,b)
    b[0] = b[0] + factor*(T[0,j]+T[0,j+1])
    b[-1] = b[-1] + factor*(T[-1,j]+T[-1,j+1])
    solution = np.linalg.solve(A,b)
    T[1:-1,j+1] = solution
print(A.round(3))
print(T.round(3))
R = np.linspace(1,0,m)
B = np.linspace(0,1,m)
G = 0
for j in range(m):
    plt.plot(x,T[:,j], color = [R[j],G,B[j]])
plt.legend([f"t = {value}s" for value in t.round(3)])
plt.xlabel("Distance")
plt.ylabel("Temperature")
plt.show()