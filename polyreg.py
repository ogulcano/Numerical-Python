import numpy as np
import matplotlib.pyplot as plt

x = np.array([-1.2,0.7,2.1,3.5,4.2,5.6,7.3])
y = np.array([-0.72,1.2,1.5,3.1,4.2,7.2,6.8])
err = []
for d in range(0,20):
    M = np.zeros(shape=(len(x),d+1))
    for i in range(len(x)):
            for j in range(0,d+1):
                M[i,j] = np.power(x[i],j)

    coeffns = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(M),M)),np.transpose(M)),y)
    #print(coeffns)
    xn = np.linspace(-3,3)
    f = np.polynomial.Polynomial(coeffns)
    error = y - np.matmul(M,coeffns)
    er = 0
    for i in range(len(error)):
         er += np.power(error[i],2)
    err.append(np.power(er,0.5))
ind = err.index(min(err))

M = np.zeros(shape=(len(x),ind+1))
for i in range(len(x)):
        for j in range(0,ind+1):
            M[i,j] = np.power(x[i],j)

coeffns = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(M),M)),np.transpose(M)),y)
print("Total number of data points:",len(x))
print("Degree of Polynomial:",ind)
print("Coefficients of Polynomial:\n",coeffns)
print("The error:",err[ind])

xn = np.linspace(np.min(x),np.max(x))
f = np.polynomial.Polynomial(coeffns)

plt.plot(xn,f(xn))
plt.plot(x,y,"*")
plt.show()


