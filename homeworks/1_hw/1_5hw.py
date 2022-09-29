#5. Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.
#  https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
#in
#- 3
#- 6
#- 2
#- 1
#out
#5.099

def Enter(text):
    while True:
        try:
            x = float(int(input(f"Введите значение {text}: ")))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            break
    return x

coordinats = []
for i in range(4):
    if i % 2 ==0:
        coordinats.append(Enter("X"))
    else:
        coordinats.append(Enter("Y"))
distance_between_2_points=round(((coordinats[0]-coordinats[2])**2+(coordinats[1]-coordinats[3])**2)**0.5, 3)
print("Расстояние между двумя точками = ", distance_between_2_points)

# Странный вариант округления, рассмотренный на занятии
#x_1 = int(input())
#y_1 = int(input())
#x_2 = int(input())
#y_2 = int(input())
#print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}")
