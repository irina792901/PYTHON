#2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE in Enter the name of the file with the text: 'text_words.txt'
# Enter the file name to record: 'text_code_words.txt'
# Enter the name of the file to decode: 'text_code_words.txt'
# out aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
# out in file 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
# 'text_code_words.txt
# '5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q


def RLE_coding(file_from, file_to):
    with open(file_from, 'r', encoding='utf-8') as foo:
        lines = foo.readlines()
        for line in lines:
            pure_line = line.strip()
            with open(file_to, 'a', encoding='utf-8') as too:
                i = 0
                code = ''
                while i < len(pure_line):
                    count = 1
                    while i + 1 < len(pure_line) and pure_line[i] == pure_line[i + 1]:
                        count += 1
                        i += 1
                    code += str(count) + pure_line[i]
                    i += 1
                for i in range(len(code)):
                    too.write(f'{code[i]}')
                too.write('\n')

def RLE_decoding(file_from):
    code = ''
    count = ''
    with open(file_from, 'r', encoding='utf-8') as foo:
        lines = foo.readlines()
        for line in lines:
            pure_line = line.strip()
            for char in pure_line:
                if char.isdigit():
                    count += char
                else:
                    code += char * int(count)
                    count = ''
            print(code)
            code = ''


file_from = input("Enter the name of the file with the text: ")
file_to = input("Enter the file name to record: ")
RLE_coding(file_from, file_to)
RLE_decoding(file_to)

