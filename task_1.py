base = int(input('Введите количество времени для конвертации в секундах: '))
if base < 59:
    seconds = base
    print(f'Сюрприз, {base} секунд это {seconds} секунд! Вот это поворот!')
elif base < 3599:
    seconds = base % 60
    minutes = base // 60
    print(f'{base} секунд это {minutes} минут,{seconds} секунд.')
elif base < 86399:
    seconds = base % 60
    hours = base // 3600
    minutes = (base - hours * 3600 - seconds) // 60
    print(f'{base} секунд это {hours} часов, {minutes} минут,{seconds} секунд.')
elif base < 2591999:
    seconds = base % 60
    days = base // 86400
    hours = (base - days * 86400 - seconds) // 3600
    minutes = (base - days * 86400 - hours * 3600 - seconds) // 60
    print(f'{base} секунд это {days} дней, {hours} часов, {minutes} минут,{seconds} секунд.')
#Задание со звездочкой, месяцы и годы, если мы считаем, что в месяце 30 дней, а в году - 365
elif base < 32535999:
    seconds = base % 60
    months = base // 2592000
    days = (base - months * 2592000 - seconds) // 86400
    hours = (base - months * 2592000 - days * 86400) // 3600
    minutes = (base - months * 2592000 - days * 86400 - hours * 3600) // 60
    print(f'{base} секунд это {months} месяцев, {days} дней, {hours} часов, {minutes} минут,{seconds} секунд.')
else:
    seconds = base % 60
    years = base // 32536000
    months = (base - years * 32536000) // 2592000
    days = (base - years * 32536000 - months * 2592000 - seconds) // 86400
    hours = (base - years * 32536000 - months * 2592000 - days * 86400) // 3600
    minutes = (base - years * 32536000 - months * 2592000 - days * 86400 - hours * 3600) // 60
    print(f'{base} секунд это {years} лет, {months} месяцев, {days} дней, {hours} часов, {minutes} минут,{seconds} секунд.')


