#* 4. Напишите программу, которая принимает на вход 2 числа. Задайте список 
# из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях(не индексах).
#Position one: 1
#Position two: 3
#Number of elements: 5
#-> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
#-> 15


def get_list_from_N_to_N(number):
    list = []
    number2 = number + 1
    step = 1
    if number < 0:
        number2 = number - 1
        step = -1
    for i in range (-number, number2, step):
        list.append(i)
    return list


def Enter(text, length):
    while True:
            try:
                x = int(input(f"{text}"))
                if 1 <= x <= length:
                    break
                else:
                    print("Position does not exist") 
                    continue
            except ValueError:
                print("Sorry, I didn't understand that.")   
                continue
    return x



num = int(input("Number of elements: "))
list_from_number = get_list_from_N_to_N(num)
length = len(list_from_number)
position1 = Enter("Position one: ", length)
position2 = Enter("Position two: ", length)
print(list_from_number)
print(list_from_number[position1-1]*list_from_number[position2-1])

