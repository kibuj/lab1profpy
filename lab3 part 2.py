import numpy as np

def matrix_list(rows, colums, a, b):
    matrix = np.random.randint(a, b, (rows, colums))

    return matrix

def count(matrix):
    list = matrix[1]
    print(list)


a,b,c,d,e,g = 0, 2, -10, 11, 0, 21
firstex = matrix_list(6,13, a, b)
secondex = matrix_list(6,13, c, d)
thridex = matrix_list(6,13, e, g)

a = count(matrix_list(firstex, secondex, a, b))



print("-" * 60)
print(f"{firstex}\n")
print("-" * 60)
print(f"{secondex}\n")
print("-" * 60)
print(f"{thridex}")
