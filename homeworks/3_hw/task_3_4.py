# 4. * Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
#      Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform


def list_rand_nums(count: int):
    list_nums = []
    if count <= 0:
        print("Negative value of the number of numbers!")
        return [0.0]

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums


def dif_max_min(list_nums: list):
    num_max = num_min = list_nums[0] % 1

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2)
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2)
    print(f"Min: {num_min}, Max: {num_max}. Difference: {result}")
    return result


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(dif_max_min(all_list))