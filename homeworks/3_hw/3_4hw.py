#4.* Задайте список из произвольных вещественных чисел, количество 
# задаёт пользователь. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части 
# элементов.
# in 5 out [5.16, 8.62, 6.57, 7.92, 9.22] 
# Min: 0.16, Max: 0.92. Difference: 0.76
# in 3 out [9.26, 8.5, 1.14] Min: 0.14, Max: 0.5. Difference: 0.36

#--------вариант 1 с использованием list(map)

from audioop import minmax
import random
from sys import maxunicode
def function_fractional_part(floater):
    '''Функция отделяет дробную часть 
    
    у вещественных элементов списка'''
    return round(floater % 1, 5)

number = int(input("Введите количество элементов списка: "))
fractional_list = [round(random.uniform(10, 100), 3) for i in range(number)] 
#list2 = list(map(function_fractional_part, fractional_list))
#minimum = min(list2)
#maximum = max(list2)
#print(fractional_list)
#print(f"Min: {minimum}, Max: {maximum}, Difference: {round(maximum-minimum, 5)}")

#-------- вариант 2 с использованием понимания списка (меняется только 
# строка 22 и это работает!)
 
#list2 = [function_fractional_part(i) for i in fractional_list]

#-------- варианте 3 с использованием лямбды-функции 
# (как я её поняла) с 22 строки меняем на следующее:

list2 = [(lambda x: round(x % 1, 5))(x) for x in fractional_list]
print(list2)
minimum = list2[0]
maximum = list2[number-1]
difference = round(maximum - minimum, 5)
print(f"Min: {minimum}, Max: {maximum}, Difference: {difference}")
