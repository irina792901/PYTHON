 #4.* Задана натуральная степень k. Сформировать случайным образом список 
 # коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен 
 # не менее 3-х раз.
 # in 9 5 3 out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# in 0 -1 4 out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0
# 2*x^4 - 3*x^3 + 3*x^2 + 1*x^1 - 2 = 0

from random import sample, choice

def polynomial(num):
    if num < 1:
        return 0

    poly = ""
    lst = sample(range(0, 20), 15)

    with open("polynomial.txt", "a", encoding="utf-8") as f:
        for i in range(num, 0, -1):
            value = choice(lst)
            if value:
                poly += f"{value}*x^{i} {choice('-+')} "

        f.write(f"{poly} {value} = 0\n")


for k in range(3):
    polynomial(int(input()))