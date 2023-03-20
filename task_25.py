# # Напишите программу, которая принимает на вход
# # строку, и отслеживает, сколько раз каждый символ
# # уже встречался. Количество повторов добавляется к
# # символам с помощью постфикса формата _n.
# # Input: a a a b c a a d c d d
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

import random
import string

N = 16
letters = string.ascii_lowercase
str_rd = ' '.join(random.choice(letters) for i in range(N))
print(str_rd)

str_rd = str_rd.split(' ')
dict_result = {}
for i in str_rd:
    if i in dict_result:
        print(f'{i}_{dict_result[i]}', end=' ')
    else:
        print(i, end=' ')
    dict_result[i] = dict_result.get(i, 0) + 1