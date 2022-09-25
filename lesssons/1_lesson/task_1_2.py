# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

num_max = 0

for i in range(5):
    n = int(input())
    if n > num_max:
        num_max = n
print(num_max)
