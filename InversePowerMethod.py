import numpy as np

def InversePowerMethod(A,x,y,max_iter):
    for _ in range(max_iter):
        y = np.matmul(np.linalg.inv(A),x)
        eg = np.matmul(x,y)/np.matmul(x,x)
        x = y/np.max(y)
    return eg, x

A = np.array([[1,2,0],
              [2,0,1],
              [2,4,1]
              ])

x = np.array([1,1,1])
y = np.zeros(len(A))
eg, x = InversePowerMethod(A,x,y,20)
print(f"The eigenvalue: {eg}\nThe eigenvector: {x/np.max(np.abs(x))}")