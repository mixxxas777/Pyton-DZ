# 11. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list_1 = list(map(float, input("Введите числа через пробел:\n").split()))
list_length = len(list_1)
sum_1 = 0
j = 1
i = 1

while j < ((list_length+1)/2):
    sum_1 += list_1[i]
    i += 2
    j += 1
print (f'{list_1}  -> сумма элементов списка, стоящих на нечётной позиции: {sum_1}')

