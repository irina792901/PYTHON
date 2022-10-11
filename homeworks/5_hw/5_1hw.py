# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in Number of words: 10
# out авб абв бав абв вба бав вба абв абв абв
#     авб бав вба бав вба
# in Number of words: 6
# out ваб вба абв ваб бва абв
#     ваб вба ваб бва
# in Number of words: -1
# out The data is incorrect

from random import sample


def random_str(alphabet):
    count = int(input('Number of words: '))
    if count < 1:
        return "The data is incorrect"
    list_words = []
    for _ in range(count):
        list_words.append("".join(sample(alphabet, 3)))
    return " ".join(list_words)


def remove_words(lst, alp):
    return lst.replace(alp, "").replace("  ", " ").strip()

string = random_str("абв")
print(string)
print(remove_words(string, "абв"))

