import numpy as np

def cholesky(a):
    a = np.array(a,float)
    L = np.zeros_like(a)
    n,_ = np.shape(a)
    for j in range(n):
        for i in range(j,n):
            if i == j:
                sumk = 0
                for k in range(j):
                    sumk += L[i,k]**2
                L[i,j] = np.sqrt(a[i,j]-sumk)
            else:
                sumk = 0
                for k in range(j):
                    sumk += L[i,k]*L[j,k]
                L[i,j] = (a[i,j] - sumk)/L[j,j]
    return L

def solveLU(L,U,b):
    L = np.array(L,float)
    U = np.array(U,float)
    b = np.array(b,float)
    n,_ = np.shape(L)
    y = np.zeros(n)
    x = np.zeros(n)

    # Forward
    for i in range(n):
        sumj = 0
        for j in range(i):
            sumj += L[i,j]*y[j]
        y[i] = (b[i] - sumj)/L[i,i]
    
    # Backward
    for i in range(n-1,-1,-1):
        sumj = 0
        for j in range(i+1,n):
            sumj += U[i,j]*x[j]
        x[i] = (y[i] - sumj)/U[i,i]
    return x


H = [
    [10,2,1],
    [2,10,3],
    [1,3,10]
]
b = [1,9,11]
H_new = cholesky(H)
print(H_new)

soln = solveLU(H_new,np.transpose(H_new),b)

print(soln)