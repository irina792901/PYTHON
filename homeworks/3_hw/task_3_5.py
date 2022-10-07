# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def neg_fib(num: int):
    a, b = 1, 1
    list_nums = [0]

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return list_nums


print(*neg_fib(int(input())))
