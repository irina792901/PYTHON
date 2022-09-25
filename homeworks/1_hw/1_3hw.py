#3. Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти 
# плоскости, в которой находится эта точка (или на какой 
# оси она находится).
#*Пример:*
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

def Enter(text):
    while True:
            try:
                x=float(input(f"Введите координату точки по оси {text}: "))
            except ValueError:
                print("Sorry, I didn't understand that.")   
                continue
            else:
                break
    return x


x = Enter("X")
y = Enter("Y") 
   
if x==0 or y==0:
    answer="Точка находится на оси "
    if x==0 and y==0:
        print("Error, 0 0 entered!")
    elif x==0 and y!=0:
        print(answer,"Y")
    elif y==0 and x!=0:
        print(answer, "X")
else:
    if x>0:
        if y>0:
            answer = 1
        elif y<0:
            answer = 4
    elif x<0:
        if y>0:
            answer = 2
        elif y<0:
            answer = 2
    print("Точка находится в {} четверти плоскости".format(answer))

