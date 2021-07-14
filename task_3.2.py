def translate(number):
    for key, val in num_list.items():
        if number.lower() == key:
            if number[0].isupper():
                number.lower()
                return val.capitalize()
            else:
                return val

num_list = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}

print(f'Ваше число: {translate(input("Enter your number in english: "))}')

