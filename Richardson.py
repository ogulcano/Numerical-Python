import numpy as np

A = np.array([[6,1,1],
              [2,4,8],
              [1,2,6]
              ])
b = np.array([7,6,-1])
n = len(b)

x0 = np.zeros(n)
x1 = np.zeros(n)
for _ in range(100):
    for i in range(n):
        k = 0
        for j in range(n):        
            k += A[i,j]*x0[j]
        x1[i] = x1[i] + (1/np.max(A))*(b[i] - k)
    x0 = x1
print(x0.round(5))
print(np.abs(np.sum((x0-x1))))