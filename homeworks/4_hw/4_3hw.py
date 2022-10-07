#3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности в том же порядке.
# in 7 out [4, 5, 3, 3, 4, 1, 2] [5, 1, 2]
# in -1 out Negative value of the number of numbers! []
# in 10 out [4, 4, 5, 5, 6, 2, 3, 0, 9, 4] [6, 2, 3, 0, 9]

from random import randint

def random_lst(number):
    if number < 0:
        print('Negative value of the number of numbers!')
        return []
    new_lst = [randint(1, number) for i in range(number)]
    print(new_lst)
    return new_lst


def array_without_repeats(some_lst):
    new_lst = []
    for i in range(len(some_lst)):
        count = some_lst.count(some_lst[i])
        if count == 1:
            new_lst.append(some_lst[i])
    return new_lst

num = int(input("Введите число, обозначающее размер списка: "))
print(array_without_repeats(random_lst(num)))

