from lab5 import np

def compute_y(t):
    if 2.3 <= t <= 7.2:
        return (np.cos(t**2) ** 3) / (1.5 * t + 2)
    else:
        return None

t = 2.3
delta_t = 0.8


while t <= 7.2:
    y = compute_y(t)
    if y is not None:
        print(f"t = {t:.1f}, y = {y:.6f}")
    t += delta_t
