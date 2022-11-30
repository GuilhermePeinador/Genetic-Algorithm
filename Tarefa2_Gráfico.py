import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-4*np.pi, 4*np.pi, 0.01)
y = x*np.sin(3*x)
line, = plt.plot(x, y)

plt.show()

