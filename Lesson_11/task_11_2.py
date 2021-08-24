class WrongDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


division = input('Введите два числа - делимое и делитель, через запятую: ')
try:
    res = map(int, division.split(','))
    res = list(res)
    print(res)
    if res[1] == 0:
        raise WrongDivision
except WrongDivision:
    print('OOPS ITS AN ERROR BRO')
else:
    print(f'Результат: {res[0]/res[1]}')

