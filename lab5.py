import numpy as np

# Перше завдання
def average(n):
    count = len(n)
    total = sum(n)

    return total/count


def taylor_series(x, epsilon):
    term = 1
    sum_taylor = term
    n = 1

    while abs(term) > epsilon:
        term *= x
        sum_taylor += term
        n += 1

    return sum_taylor, n



print(f"Перше завдання: \n{average([1,2,3,4,5,6,7])}\n")


a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
epsilon = float(input("Введіть точність ε: "))

num_points = max(10, int(abs(b - a) * 10))
x_values = np.linspace(a, b, num_points)

print(f"{'x':^10} | {'f(x) точне':^15} | {'f_Taylor(x)':^15} | {'ε':^10} | {'Ітерації':^10}")
print("-" * 65)

for x in x_values:
    if abs(x) >= 1:
        print(f"{x:^10.4f} | {'Неможливо обчислити':^15} | {'-':^15} | {'-':^10} | {'-':^10}")
        continue

    exact_value = 1 / (1 - x)
    taylor_value, iterations = taylor_series(x, epsilon)
    error = abs(exact_value - taylor_value)

    print(f"{x:^10.4f} | {exact_value:^15.8f} | {taylor_value:^15.8f} | {error:^10.8f} | {iterations:^10}")




