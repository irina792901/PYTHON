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

