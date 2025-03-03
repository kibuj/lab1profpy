from main import np

def first_ex(x):
    f_x = x * np.log(x)
    y = np.arcsin(abs(1+np.cos(x)))

    return f_x, y

x = 2
f_x, y = first_ex(x)

print(f_x, y)