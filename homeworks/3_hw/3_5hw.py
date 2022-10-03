#5. ** Задайте число. Составьте список чисел 
# Фибоначчи, в том числе для отрицательных 
# индексов Негафибоначчи
# in 8 out -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in 5 out 5 -3 2 -1 1 0 1 1 2 3 5

def fibonacci(n: int):
    list = [0]*(2*n+1)
    list[n-1] = 1
    list[n] = 0
    list[n+1] = 1
    for i in range (2, n + 1):
        list[n+i] = list[n+i-2] + list[n+i-1]
        list[n-i] = list[n-i+2] - list[n-i+1]
    return list    

num = int(input("Задайте число для определения длины последовательности Фибоначчи: "))
if num < 2: print("Вы ввели слишком маленькое число для задания последовательности Фибоначчи") 
list_fibonacci = fibonacci(num)
print(' '.join(str(x) for x in list_fibonacci)) 
 