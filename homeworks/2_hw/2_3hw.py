#3. Задайте список из n чисел, заполненный по формуле 
# (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

num = int(input())
list = []
sum = 0
for i in range(1, num+1):
    formula = round((1+1/i)**i)
    list.append(formula)
    sum += formula
print(list, "->", sum)


