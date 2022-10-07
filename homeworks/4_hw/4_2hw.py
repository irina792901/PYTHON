#2. Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.
# Простые делители числа
# in 54 out [2, 3, 3, 3]
# in 9990 out [2, 3, 3, 3, 5, 37]
# in 650 out [2, 5, 5, 13]

def prime_factors(number):
    lst = []
    simple = 2
    while number > 1:
        if not number % simple:
            lst.append(simple)
            number //= simple
        else:
            simple +=1
    return lst

print(prime_factors(int(input("Введите целое число N: "))))
