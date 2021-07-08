base = int(input('Введите количество времени для конвертации в секундах:'))

# 60 = 1 minute
# 3600 = 1 hour
# 86400 = 1 day
# 2592000 = 1 month
# 31536000 = 1 year

seconds = base % 60
years = base // 31536000
months = (base - years * 31536000) // 2592000
days = (base - years * 31536000 - months * 2592000) // 86400
hours = (base - years * 31536000 - months * 2592000 - days * 86400) // 3600
minutes = (base - years * 31536000 - months * 2592000 - days * 86400 - hours * 3600) // 60

text = ''

if years != 0:
    text = text + f' {years} years '
if months != 0:
    text = text + f' {months} months '
if days != 0:
    text = text + f' {days} days '
if hours != 0:
    text = text + f' {hours} hours '
if minutes != 0:
    text = text + f' {minutes} minutes '
if seconds != 0:
    text = text + f' {seconds} seconds'
print(text)

