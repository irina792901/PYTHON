# 4. * Напишите программу, которая принимает на вход 2 числа.
#      Получите значение N, для пустого списка, заполните числами
#      в диапазоне [-N, N]. Найдите произведение элементов
#      на указанных позициях(не индексах).

num = int(input("Enter the value of N: "))
n_1 = int(input("Position one: "))
n_2 = int(input("Position two: "))

nums_list = list(range(-num, num + 1))

print(nums_list)
len_list = len(nums_list)

if len_list >= n_1 > 0 and len_list >= n_2 > 0:
    print(nums_list[n_1 - 1] * nums_list[n_2 - 1])
else:
    print("There are no values for these indexes!")
