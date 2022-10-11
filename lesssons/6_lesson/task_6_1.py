# Напишите программу вычисления арифметического выражения, заданного строкой. 
# Используйте операции +,-,/,* приоритет операций стандартный. Добавьте скобки 
# и приоритет опарций метяется.
# 

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}


# Ищем скобки, обосабливаем в списки
def parse(exp_1):
    pr_list = []
    i = 0

    while i < len(exp_1):
        if exp_1[i] == "(":
            n_2 = exp_1.index(")", i)
            pr_list.append(exp_1[i + 1: n_2])
            i = n_2
        else:
            pr_list.append(exp_1[i])
        i += 1
    return pr_list


# Результирующая функция
# TODO доработать
def decision(final_list: list):
    # Получение индексов приоритетных операций
    ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

    # Работа с приоритетными операциями
    while ind_list:
        k = ind_list[0]
        a, s, b = final_list[k - 1: k + 2]
        final_list.insert(k - 1, actions[s](a, b))
        del final_list[k:k + 3]
        ind_list = [i for i, v in enumerate(final_list) if v in "*/"]

    i = 0
    # Работа с оставшимися операциями
    while len(final_list) > 2:
        a, s, b = final_list[:3]
        del final_list[:3]
        final_list.insert(i, actions[s](a, b))
        i = 0

    return final_list[0]


# Раскрываем скобки
def exp_brackets(some_list):
    for i, v in enumerate(some_list):
        if isinstance(v, list):
            some_list[i] = decision(v)
    return some_list


# exp = "4 * 3 - 1 / 9 - 7 * -1".split()
exp = "-2 + ( 4 / 2 - 7 + 8 * 7 ) * 3".split()
# exp = "( 12 + 8 ) * 3 - 11 / 2".split()
# exp = "11 / 2 - ( 12 + 8 ) * 3".split()
# exp = "5 + 11 / 2 - ( 12 + 8 ) * 3 - 12".split()
# exp = "4 * ( 3 - 1 ) / ( 9 - 7 ) * -1".split()
# exp = "8 + 2 * 4 + ( 6 + ( 2 - 3 ) * 2 )".split()  # 1

pr_list = exp_brackets(parse(exp))
print(pr_list)
print(decision(pr_list))
