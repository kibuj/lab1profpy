import matplotlib.pyplot as plt
import numpy as np


def y(x):
    return 5 * np.sin(10 * x) * np.sin(3 * x)


x = np.linspace(0, 4, 1000)  # 1000 точок на інтервалі [0, 4]
y_values = y(x)


plt.plot(x, y_values, 'b-', label='Y(x) = 5·sin(10x)·sin(3x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x) = 5·sin(10x)·sin(3x)')
plt.grid(True)
plt.legend(loc='upper right')


plt.savefig("graph.png")

plt.show()
