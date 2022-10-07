# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#    Без использования: встроенной функции преобразования, строк.

def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2

    print(*list_nums, sep="")


conv_bin(int(input()))
