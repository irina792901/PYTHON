# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. 
# Use comprehension.
# in 100 out [20, 21, 40, 42, 60, 63, 80, 84, 100]
# in 424 out [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 
# 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 
# 336, 340, 357, 360, 378, 380, 399, 400, 420]

#----------1 вариант фильтром из списка выбрать элементы 

# def multiples(num, num1 = 20):
#     res = [i for i in range(num1, num + 1)]
#     res = list(filter(lambda x: x % 20 ==0 or x % 21 == 0, res))
#     return res

# print(multiples(int(input("Enter the real number: "))))

#-----------2 вариант сразу черзе list comprehention (этот более понятен))

def multiples(num, num1 = 20):
    res = [i for i in range(num1, num + 1) if i % 20 == 0 or i % 21 == 0] 
    return res

print(multiples(int(input("Enter the real number: "))))

