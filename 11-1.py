import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi)
y = np.sin(x)

plt.xlim([0, np.pi])
plt.ylim([0, 1])

plt.plot(x, y)
plt.show()