#3. Написать функцию, аргументы имена сотрудников, возвращает словарь, 
# ключи — первые буквы имён, значения — списки, содержащие имена, 
# начинающиеся с соответствующей буквы.
# in "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 
# 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

#--------вариант 1 всё в одном

# from itertools import groupby

# def get_dictionary(lst: list):
#     res = {k:list(g) for k, g in groupby(sorted(lst), key = lambda x: x[0])}
#     return res

# print(get_dictionary(list(input("Enter the names separated by a space: ").split())))


#---------вариант второй через setdefault


# def my_dict(lst):
#     res = {}
#     for i, j in lst:
#         res.setdefault(i[0], []).append(j)
#     sorted(res.items())
#     return res

# line = ''
# names = []
# while line != 'esq':
#     line = input('Введите имя. Для окончания введите esq. ')
#     if line != 'esq':
#         names.append((line[0], line))

# print(my_dict(names))

#----------вариант 3 через циклы


def my_dict(lst):
    lst.sort()
    pre_keys=[i[0] for i in lst]
    keys=[]
    for i in range(len(pre_keys)):
        if not pre_keys[i] in keys:
            keys.append(pre_keys[i])
    res={}
    for i in range(len(keys)):
        res[keys[i]]=[]
    for k in range(len(keys)):
        for v in range(len(lst)):
            if lst[v][0]==keys[k]:
                res[keys[k]].append(lst[v])
    return res

names=input('Имена сотрудников, через запятую: ').split(',')

print(my_dict(names))