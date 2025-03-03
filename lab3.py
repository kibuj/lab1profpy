from main import random

def first_list(x):
    list_a = []

    for i in range(x):
        n = random.randint(0,1)
        list_a.append(n)
    return list_a

def second_list(y):
    list_b = []

    for i in range(y):
        n = random.randint(-10,10)
        list_b.append(n)
    return list_b

def third_list(z):
    list_c = []

    for i in range(z):
        n = random.randint(0,50)
        list_b.append(n)
    return list_c

def calculate(list, t):
    result = 0
    for i in list:
        result = result * t + i
    return result

x = int(input("Обери кількість елементів для першого масиву\n"))
y = int(input("Обери кількість елементів для другого масиву\n"))
z = int(input("Обери кількість елементів для третього масиву\n"))
q = int(input("Який масив використати для обчислення виразу \n"))

list_a = first_list(x)
list_b = second_list(y)
list_c = second_list(z)

while q not in [1, 2, 3]:
    print("Оберіть інше число (1, 2 або 3)")
    q = int(input("Який масив використати для обчислення виразу \n"))


if q == 1:
    list_for_ex = list_a
elif q == 2:
    list_for_ex = list_b
elif q == 3:
    list_for_ex = list_c


t = int(input("Введіть значення t\n"))

result = calculate(list_for_ex, t)

print(list_a)
print(list_b)
print(list_c)
print(result)