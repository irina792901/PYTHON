# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path


def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text) and path.exists(code_text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")


def rle_decode(name):
    if path.exists(name):
        with open(name) as my_f:
            n = ""
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("The files do not exist in the system!")

# def rle_decode(name):
#     if path.exists(name):
#         with open(name) as my_f:
#             for i in my_f:
#                 word_nums = ["".join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
#                 print("".join([f"{int(word_nums[i]) * word_nums[i + 1]}" for i in range(0, len(word_nums), 2)]))
#     else:
#         print("The files do not exist in the system!")

# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
rle_decode(input("Enter the name of the file to decode: "))
