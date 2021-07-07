base = int(input('Введите количество времени для конвертации в секундах: '))
seconds = 0
minutes = 0
hours = 0
days = 0

if base < 59:
    seconds = base
    print(f'Сюрприз, {base} секунд это {seconds} секунд! Вот это поворот!')
elif base < 3599:
    seconds = base % 60
    minutes = int(base / 60)
    print(f'{base} секунд это {minutes} минут,{seconds} секунд.')
elif base < 86399:
    seconds = base % 60
    hours = int(base / 3600)
    minutes = int((base - hours * 3600 - seconds) / 60)
    print(f'{base} секунд это {hours} часов, {minutes} минут,{seconds} секунд.')
else:
    seconds = base % 60
    days = int(base / 86400)
    hours = int((base - days * 86400 - seconds) / 3600)
    minutes = int((base - days * 86400 - hours * 3600 - seconds) / 60)
    print(f'{base} секунд это {days} дней, {hours} часов, {minutes} минут,{seconds} секунд.')



