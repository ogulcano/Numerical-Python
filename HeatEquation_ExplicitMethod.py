# Heat Equation // Numerical Solution // Explicit Method
import numpy as np
import matplotlib.pyplot as plt

a = 0.7 #Diffusion Constant
h = 0.1 # Delta-x
k = 0.002 # Delta-t
gamma = a*k/h**2 # Gamma < 1/2 
tv = 0.05 # Upper t-value
xv = 1.0 # Upper x-value
max_x = int(xv/h + 1) # Iteration for x
max_t = int(tv/k + 1) # Iteration for t
z = np.zeros([max_t,max_x]) # Heat Equation Values

# Boundary conditions
z[:,0] = 0  
z[:,-1] = 0 
for j in range(1,max_x):
    z[0,j] = np.sin(h*j*np.pi)

# Numerical Solution 
for i in range(1,max_t):
    for j in range(1,max_x-1):
        z[i,j] = gamma*z[i-1,j-1] + (1-2*gamma)*z[i-1,j] + gamma*z[i-1,j+1]

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



