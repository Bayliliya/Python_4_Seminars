# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

A = int(input("Введите A: "))  # кол-во элементов в 1-м массиве
B = int(input("Введите B: "))  # кол-во элементов во 2-м массиве

list_A = []
list_B = []

for i in range(A):
    list_A.append(random.randint(-10, 10))

for i in range(B):
    list_B.append(random.randint(-10, 10))

print(f'Массив_A: {list_A}')
print(f'Массив_B: {list_B}')

list_result = []

for i in list_A:
    for k in list_B:
        if i == k and i not in list_result:
            list_result.append(i)
print(f"Искомый массив: {sorted(list_result)}")
