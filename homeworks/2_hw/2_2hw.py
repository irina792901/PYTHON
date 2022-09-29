#2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]
#-----------------вариант 1 циклом

num = input()
list = []
mult = 1
for i in range(1, int(num)+1):
    mult *= i
    list.append(mult)
print(list)

#------------------вариант 2 рекурсией САМА УДИВЛЯЮСЬ, НО ТОЖЕ РАБОТАЕТ!!!

def get_multiply_from_number(k):
        if k==1:
            answer =  1
        else:
            answer = k*get_multiply_from_number(k-1)
        return answer
  
num = int(input())
list = []
while num !=0:
    list.append(get_multiply_from_number(num))
    num-=1
print(list[::-1])
