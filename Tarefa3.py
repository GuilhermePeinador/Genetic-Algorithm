from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(1,2,1, projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = X + Y
R = X**2 + Y**2 - 2

# Plot the surface.
surf = ax.plot_surface(X, Y, Z)
surf = ax.plot_surface(X, Y, R)

# Customize the z axis.
ax.set_zlim(-10,10)


plt.show()