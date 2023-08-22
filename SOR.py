import numpy as np

A = np.array([[5,2,0],
              [4,-7,-3],
              [1,-1,5]
              ])
b = np.array([12,-10,8])
n = len(b)
w = 0.93
x0 = np.ones(n)
x1 = np.zeros(n)
for _ in range(10): 
    print(x0.round(10))
    for i in range(n):
        k1 = 0
        for j in range(i):      
            k1 += A[i,j]*x1[j]
        k2 = 0
        for j in range(i+1,n):
            k2 += A[i,j]*x0[j]
        x1[i] = (w/A[i,i])*(b[i] - k1 - k2) + (1-w)*x0[i]
    x0 = x1