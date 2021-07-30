from random import randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def jokes(number):
    jokes_list = []
    i = 0
    while i < int(number):
        nouns_n = randint(0, len(nouns)-1)
        adv_n = randint(0, len(adverbs)-1)
        adj_n = randint(0, len(adjectives)-1)
        jokes_list.append(f'{nouns[nouns_n]} {adverbs[adv_n]} {adjectives[adj_n]}')
        i += 1
    return jokes_list


print(jokes(input('Введите количество шуток: ')))
