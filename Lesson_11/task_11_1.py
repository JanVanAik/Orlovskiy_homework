import re

class RangeError(Exception):
    def __init__(self, txt='Wrong Range' ):
        self.txt = txt

class Data:
    def __init__(self, date):
        self.date = date

    def pulse(self):
        print(self.date)

    @classmethod
    def extractor(cls, data):
        date_list = data.split('.')
        d = int(date_list[0])
        m = int(date_list[1])
        y = int(date_list[2])
        return f'day = {d}, {type(d)}\nmonth = {m}, {type(m)}\nyear = {y}, {type(y)}'

    @staticmethod
    def validator(data):
        res = data.split('.')
        if 1 <= int(res[0]) <= 31:
            if 1 <= int(res[1]) <=12:
                if 1900 <= int(res[2]) <= 2021:
                    return data
        else:
            raise RangeError


def is_valid(date):
    if RE_DATE.match(date):
        return date
    else:
        raise TypeError


RE_DATE = re.compile(r'^(\d{2}\.){2}\d{4}$')
try:
    #is_valid проверяет, что дата в виде дд.мм.гггг
    #validator(classmethod) - что день находится в промежутке 1-31, месяц 1-12, год 1900-2021
    user_date = Data(Data.validator(is_valid(input('Введите дату в форме дд.мм.гггг: '))))
except TypeError:
    print('Вы ввели дату в неверном формате')
except RangeError:
    print('Вы ввели дату в некорректном диапазоне')
else:
    print('Data is using correct form and is in valid data range.')
    print(user_date.date)
    print(user_date.extractor(user_date.date))