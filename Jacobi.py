import numpy as np

A = np.array([[4,0,1],
              [1,4,1],
              [1,0,4]
              ])
b = np.array([3,-1,2])
n = len(b)

x0 = np.ones(n)
x1 = np.zeros(n)
for _ in range(15): 
    print(x0.round(10))
    for i in range(n):
        k = 0
        for j in range(n):
            if i == j:       
                k += 0
            else:
                k += A[i,j]*x0[j]
            x1[i] = (1/A[i,i])*(b[i] - k)
    x0 = x1
    