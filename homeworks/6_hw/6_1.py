#1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in 9 out [15, 16, 2, 3, 1, 7, 5, 4, 10] [16, 3, 7, 10]
# in 10 out [28, 20, 10, 5, 1, 24, 7, 15, 23, 25] [24, 15, 23, 25]

from random import randint

def enter(text):
    while True:
        try:
            number = int(input(f"{text}"))
        except ValueError:
            print("Sorry, i didn't underxtand that.")
            continue
        else:
            break
    return number

def from_less_to_more(count):
    rand_numbers_list = [randint(0, 10) for _ in range(count)]
    print(rand_numbers_list)
    rand_numbers_list = [rand_numbers_list [i+1] \
        for i in range(len(rand_numbers_list)-1) 
        if rand_numbers_list [i+1] > rand_numbers_list[i]]    
    return rand_numbers_list    

number = enter("Enter the number of array elements: ")
print(from_less_to_more(number))
   
