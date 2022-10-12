# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех 
# случайных слов, взятых из трёх списков (по одному из каждого)
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# in 10 True out ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 
# 'автомобиль сегодня веселый', 'город позавчера утопичный']
# in 10 False ['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 
# 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 
# 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']


from random import sample, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

joke1 = sample(nouns, len(nouns))
joke2 = sample(adverbs, len(adjectives))
joke3 = sample(adjectives, len(adjectives))

user_number = int(input('Введите количество шуток: '))

replay = ''

while replay != 'True' or replay != 'False':
    replay = input('Могут ли слова шуток повторяться? Если "Да", введите "False", если "Нет", введите "True" ')
    if replay == 'True' or replay == 'False':
        break

if replay == 'True':
    rep = True
if replay == 'False':
    rep = False

if not rep:
    joke = [choice(joke1) + ' ' + choice(joke2) + ' ' + choice(joke3) for i in range(user_number)]
else:
    x = len(joke1)
    if len(joke2) < x:
        x = len(joke2)
    if len(joke3) < x:
        x = len(joke3)
    joke = [joke1[i] + ' ' + joke2[i] + ' ' + joke3[i] for i in range(x)]

print(joke)




