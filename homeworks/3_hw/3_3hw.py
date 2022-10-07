#3. Напишите программу, которая будет преобразовывать десятичное 
# число в двоичное. Без использования встроенной функции 
# преобразования, без строк.
# in 88 out 1011000
# in 11 out 1011

def from_decimal_to_bin(number):
    '''Переводит десятичные числа в двоичные
    
    в т.ч. отрицательные и дробные
    '''
    list= []
    if number < 0:
        x = abs(number)-1 #Если число отрицательное
    else:
        x = number
    x = int(x)
    while x > 0:
        list.insert(0, x%2)
        x //= 2
    y = abs(number) % 1 # Если чилсо дробное
    if y > 0:
        list.append('.')
        count = 0
        while y > 0 and count < 10:
            k = int((y*2))
            list.append(k)
            y = (y * 2) % 1
            count +=1
    if number < 0:
        list.insert(0, 1) # Есил число отрицательное, то впереди ставится единица
    print(''.join(str(x) for x in list))
              
from_decimal_to_bin((float(input("Введите число: "))))

