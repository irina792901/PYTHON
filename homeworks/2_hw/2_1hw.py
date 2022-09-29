# 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
#in -> out
#- 6782 -> 23
#- 0.67 -> 13
#- 198.45 -> 27


#-------------------вариант 1 "просто через .replace()" THE BEST

num = str(input())
sum = 0
if "." in num:
    num = num.replace('.', '')
while num != str():
    sum += int(num[0])
    num = num.replace(num[0],"")
print("Сумма цифр = ", sum)

#--------------------вариант 2 "математический"

num = (input())
sum = 0
length = len(num)
if str(num).find('.') >= 0:
    length -=1
    num = float(num)*10**(length-num.find('.'))
num = int(num) 
for i in range(length):
    sum +=num % 10
    num //=10
print(sum)
