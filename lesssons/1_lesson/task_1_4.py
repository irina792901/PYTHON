# 4. Напишите программу, которая будет принимать на вход дробь
#    и показывать первую цифру дробной части числа.

num = float(input())
sec_num = num * 10 % 10

if sec_num != 0:
    print(int(sec_num))
else:
    print("No")
