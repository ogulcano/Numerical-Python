import numpy as np

def InversePowerMethod(A,x,y,max_iter,m):
    for _ in range(max_iter):
        y = np.matmul(np.linalg.inv(A-m*np.eye(len(A))),x)
        eg = np.matmul(x,y)/np.matmul(x,x)
        eg = 1/eg + m
        x = y/np.max(y)
    return eg, x

A = np.array([[1,2,-1],
              [1,0,1],
              [4,-4,5]
              ])
m = 2.4
iteration = 150
x = np.array([1,1,1])
y = np.zeros(len(A))
eg, x = InversePowerMethod(A,x,y,iteration,m)
print(f"The eigenvalue: {eg}\nThe eigenvector: {x/np.max(np.abs(x))}")