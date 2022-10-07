# 3. Задайте два числа. Напишите программу, которая найдёт
#    НОК (наименьшее общее кратное) этих двух чисел.

from math import gcd


def nok(a, b):
    return (a * b) // gcd(a, b)


# 14 18 -> 126, 17 11 -> 187
print(nok(int(input()), int(input())))