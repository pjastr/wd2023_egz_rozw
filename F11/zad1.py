import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 1, 0.1)
y1 = np.exp(4 * x)
y2 = 2 * np.cos(3 * x)
y3 = x ** 2 + 4
plt.plot(x, y1, color="red", linestyle=":", label="$y=e^{4x}$")
plt.plot(x, y2, color="blue", label="$y=2\cos(3x)$")
plt.plot(x, y3, color="forestgreen", linestyle="--", label="$y=x^2+4$")
plt.xticks(np.arange(-3, 2))
plt.yticks(np.arange(0, 40, 5))
plt.title("Wykres trzech funkcji")
plt.grid()
plt.legend(loc=2)
plt.savefig("zad1.webp")
plt.show()
