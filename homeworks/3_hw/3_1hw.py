#1. Задайте список, состоящий из произвольных чисел, количество 
# задаёт пользователь. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётных позициях(не индексах).
# in 5
# out [10, 2, 3, 8, 9] 22
# in 4 out [4, 2, 4, 9] 8

from random import sample

def sum_numbers_from_odd_positions(count: int):
    if count < 0:
        return "Вы ввели отрицательное число"
    list = sample(range(1, count*10), count)
    print(list)
    sum = 0
    for i in range(0, count, 2):
        sum+=list[i]
    print("Cумма элементов на нечетных позициях = ", sum)


print(sum_numbers_from_odd_positions(int(input("Введите количество элементов: "))))
