import numpy as np

def PowerMethod(A,x,y,max_iter):
    for _ in range(max_iter):
        y = np.matmul(A,x)
        eg = np.matmul(x,y)/np.matmul(x,x)
        x = y/np.max(y)
    return eg, x

A = np.array([[-1,1,1],
              [1,5,-1],
              [0,1,-3]
              ])

x = np.array([1,1,1])
y = np.zeros(len(A))
eg, x = PowerMethod(A,x,y,20)
print(f"The eigenvalue: {eg}\nThe eigenvector: {x}")