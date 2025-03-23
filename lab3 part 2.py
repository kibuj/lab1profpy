import numpy as np

def matrix_list(rows, colums, a, b):
    matrix = np.random.randint(a, b + 1, (rows, colums))

    return matrix

def variant6(matrix):
    row = matrix[1]
    neg_n = 1
    for i in row:
        if i < 0:
            neg_n = neg_n * i
    count = 0
    l = []
    for i in matrix:
        l.append(int(i[1]))
    for j in l:
        if j % 5 != 0:
            count = count + 1

    return count, neg_n

a,b,c,d,e,g = 0, 1, -10, 10, 0, 20
firstex = matrix_list(6,13, a, b)
secondex = matrix_list(6,13, c, d)
thridex = matrix_list(6,13, e, g)

fm = variant6(firstex)
sm = variant6(secondex)
tm = variant6(thridex)


print("-" * 60)
print(f"{firstex}\n")
print(fm)
print("-" * 60)
print(f"{secondex}\n")
print(sm)
print("-" * 60)
print(f"{thridex}")
print(tm)




