import numpy as np
import matplotlib.pyplot as plt

a = 0.7 #Diffusion Constant
h = 0.1 # Delta-x
k = 0.002 # Delta-t
gamma = a*k/h**2 # Gamma
tv = 0.05 # Upper t-value
xv = 1.0 # Upper x-value
max_x = int(xv/h + 1) # Iteration for x
max_t = int(tv/k + 1) # Iteration for t
z = np.zeros([max_t,max_x]) # Heat Equation Values
n = max_x - 2
m = max_t
# Matrix 
A = np.zeros([n,n])
for i in range(0,n):
    for j in range(0,n):
        if i == j:
            if i == 0 and j == 0:
                A[i,j] = (1+2*gamma)
                A[i,j+1] = -gamma
            elif i == n - 1 and j == n - 1:
                A[i,j] = (1+2*gamma)
                A[i,j-1] = -gamma           
            else:
                A[i,j] = (1+2*gamma)
                A[i,j+1] = -gamma
                A[i,j-1] = -gamma
# Boundary conditions
z[:,0] = 0
z[:,-1] = 0 
for j in range(1,max_x):
    z[0,j] = np.sin(h*j*np.pi)

for i in range(0,max_t - 1):
    for j in range(1,n):
        uIn = z[i,1:max_x-1].copy()
        uBndy = np.zeros(n)
        uBndy[0] = z[0,j]
        uBndy[-1] = z[-1,j]
    uS = np.matmul(np.linalg.inv(A),uIn + gamma*uBndy)
    z[i+1,1:max_x-1] = uS
print(z.round(3))

# Plotting 
x = np.linspace(0,xv,max_x)
t = np.linspace(0,tv,max_t)
X, Y = np.meshgrid(x,t)
ax = plt.subplot(projection="3d",computed_zorder = False)
ax.plot_surface(X,Y,z, cmap = "viridis",zorder = 0)
ax.set_xlabel("Position $X$", fontsize=12)
ax.set_ylabel("Time $t$", fontsize=12)
ax.set_zlabel("$u($X$,$t$)$",fontsize = 16)
plt.show()

