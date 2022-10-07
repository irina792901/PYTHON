# 2. Задайте натуральное число N. Напишите программу,
#    которая составит список простых множителей числа N.

def find_prime_nums(num):
    pr_fact = []
    di = 2
    while num > 1:
        if num % di == 0:
            pr_fact.append(di)
            num //= di
        else:
            di += 1
    return pr_fact


# 650, 9990, 364, 54
print(find_prime_nums(int(input())))
