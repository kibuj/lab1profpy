from lab6_part_2 import *
import random

random_n = random.randint(5,10)
numbers = [random.randint(1, 100) for i in range(random_n)]
m = 9
subsequence = [random.randint(1, 100) for j in range(m)]

print("Список:", numbers)
print("Відсортований список:", sort_list(numbers))
print("Індекс елемента n:", find_element(numbers, random_n))
print("Індекс підпослідовності :", find_subsequence(numbers, subsequence))
print("П'ять мінімальних значень:", find_min_five(numbers))
print("П'ять максимальних значень:", find_max_five(numbers))
print("Середнє арифметичне:", calculate_average(numbers))
print("Список без дублікатів:", remove_duplicates(numbers))