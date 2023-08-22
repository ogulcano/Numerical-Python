import numpy as np
a = np.array([
    [1,5,0],
    [7,5,6],
    [8,5,6]
],float)
b = np.array([5,6,8],float)
n = len(b)
x = np.zeros(n,float)
print("The Numpy Solution:",np.linalg.solve(a,b))
# Elimination
for k in range(n-1):
    if np.fabs(a[k,k]) < 1.0e-10:
        for i in range(k+1,n):
            if np.fabs(a[k,i]) > np.fabs(a[k,k]):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
                break

    for i in range(k+1,n):
        if a[i,k] == 0: continue
        factor = a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - a[i,j]*factor
        b[i] = b[k] - b[i]*factor
# Back-substitution
x[n-1] = b[n-1]/a[n-1,n-1]
for i in range(n-2,-1,-1):
    sum_ax = 0
    for j in range(i+1,n):
        sum_ax +=a[i,j]*x[j]
    x[i] = (b[i]-sum_ax)/a[i,i]
print("The Gauss solution:",x)

