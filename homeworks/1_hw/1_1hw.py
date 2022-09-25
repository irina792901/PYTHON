# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("input the day's number of the week: "))
if 0 < day < 6:
    print("Workday")
elif 5 < day < 8:
    print("Weekend")
else:
    print("It's not a day of the week")
