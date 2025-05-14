import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.linspace(0, 4, 1000)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 4)
ax.set_ylim(-6, 6)
ax.set_title("Анімація: 5·sin(10x)·sin(3x + φ)")
ax.set_xlabel("x")
ax.set_ylabel("Y(x)")

def init():
    line.set_data([], [])
    return line,

def animate(i):
    y = 5 * np.sin(10 * x) * np.sin(3 * x + i * 0.1)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              frames=100, interval=50, blit=True)

ani.save("animated.gif", writer="pillow", fps=20)
