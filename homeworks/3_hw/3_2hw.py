#2. Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, второй и 
# предпоследний и т.д.
# in 4 out [2, 5, 8, 10] [20, 40]
# in 5 out [2, 2, 4, 8, 8] [16, 16, 4]

from random import sample

def mult_first_last_to_list(number: int):
    list = sample(range(1, number*10), number)
    print(list)
    list2 = []
    index = number//2
    for i in range(index):
        list2.append(list[i]*list[-i-1])
    if number%2==1:
        list2.append(list[index])
    print(list2)


mult_first_last_to_list(int(input("Введите число элементов списка: ")))