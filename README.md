# Знакомство с языком Python в рамках курса "Разработчик" от GeekBrains
## Полезные ссылки:
* ["Поколение Python": курс для начинающих (бесплатный)](https://stepik.org/course/58852/syllabus)
* ["Поколение Python": курс для продвинутых (бесплатный)](https://stepik.org/course/68343/promo)
* ["Поколение Python": курс для профессионалов (платный)](https://stepik.org/course/82541/promo)
* [PEP 8 - руководство по написанию кода на Python](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html)
* [Руководство по языку программирования Python](https://metanit.com/python/tutorial/)
* [Алгоритмы и структуры данных на Python 3 -> Лекции на Youtube](https://www.youtube.com/playlist?list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0)
* [Алгоритмы и структуры данных на Python 3 -> Материалы курса и практические задания](https://github.com/mipt-cs/course-site-python3/wiki)


https://learnxinyminutes.com/docs/ru-ru/python-ru/

Книги
https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_1_mark_lutc/

Если программы нет, а писать надо, то есть
[Пайтон-визуализатор](https://pythontutor.com/visualize.html#mode=edit)

ПРОГРАММИРОВАНИЕ
https://www.codewars.com/
https://euler.jakumo.org/problems.html
https://acmp.ru/index.asp?main=tasks&str=%20&page=1&id_type=0

НОК
https://zaochnik.com/spravochnik/matematika/delimost/naimenshee-obschee-kratnoe-nok/

Простые делители числа
https://autogear.ru/article/371/831/chislo-prostyih-deliteley-chisla-skolko-deliteley-imeet-prostoe-chislo/
https://calc.ws/simple-num-mnoj.php?num=650

https://calc.ws/simple-num-mnoj.php?num=99990

Алгоритм RLE
https://fb.ru/article/369240/algoritm-rle-opisanie-osobennosti-pravila-i-primeryi

Эмодзи
https://unicode-table.com/ru/emoji/

Стратегии выигрыша открывается только из-под vpn
https://informatika.shkolkovo.net/catalog/igry/prostejshie-igry-poisk-vyigryshnoj-strategii

Укус питона (коротко, по теме), Лутц, Бизли и Грокаем алгоритмы - MUST HAVE!!!!!!!!!!


## FEATURES from lessons

alt+tab = переключение между окнами

√ =...**0.5

print = функция с разными параметрами вывода например
    print(i, end", ")

СТРИНГОВЫЕ

str1где.count(str2что)
strгде.count(strчто, 3_с_какого_индекса)
strгде.count(strчто, 3_с_какого, 5_по_какой_индекс)

str.replace("старое","новое")
str.replace("старое","  ")  вырезает
str.replace("старое","") склеивает

Логические аналоги:

    ≡   == эквиваленция
    V   or
    →   <=
    ^   and

**пример функции strip**

def check(str_list):
for i, num in enumerate(str_list):
str_list[i] = num.strip('.,;:?!')
if not str_list[i].replace("-", "").isdigit():
return []
return str_list


def find_max_min(nums_str: str):
list_nums = nums_str.split()
right_list = check(list_nums)

if right_list:
return min(right_list, key=int), max(right_list, key=int)
print("The data is incorrect")
return []


print(*find_max_min(input("Enter the numbers separated by a space: ")))
