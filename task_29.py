# “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”

number = int(input("number: "))
max_num = float("-inf")
while number != 0:
    if number > max_num:
        max_num = number
    number = int(input("number: "))
print(max_num)
