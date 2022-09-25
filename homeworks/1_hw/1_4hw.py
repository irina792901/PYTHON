#4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти 
#*Пример:*
#- 33 -> The quater is entered incorrectly!
#- 1 -> x > 0, y > 0

quater = int(input("Введите номер четвертки коррдинатной плоскости: ")) 
if quater not in [1,2,3,4]:
    print("The quater is entered incorrectly")
else:
    if quater == 1:
        print("x > 0, y > 0")
    elif quater ==2:
        print("x < 0, y > 0")
    elif quater ==3:
        print("x < 0, y < 0")
    elif quater ==4:
        print("x > 0, y < 0")