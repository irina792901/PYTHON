#5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля 
# random.
#10
#-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

def Enter(text):
    while True:
            try:
                x = abs(int(input(f"{text}")))
                if x == 0:
                    print("Вы ввели 0, попытайтесь ещё раз")
                    continue
                else:
                    break 
            except ValueError:
                print("Sorry, I didn't understand that.")   
                continue
    return x

def get_list_from_0_to_N(number):
    list = []
    for i in range(number):
        list.append(i)
    return list

def mixed_list(list, number):
    new_list = []
    new_list.extend(list)
    for i in range(number):
        while new_list[i]==list[i]:
            j = random.randint(0, number-1)
            new_list[i], new_list[j] = new_list[j], new_list[i]
    return new_list

num = Enter("Введите целое положительное число N: ")
list_from_number = get_list_from_0_to_N(num)
new_list = mixed_list(list_from_number, num)
print(list_from_number)
print(new_list)

