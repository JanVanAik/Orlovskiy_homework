#реализация с любым числом
user_number = input('Введите число: ')
user_list = list(user_number)
print(user_list)
percent = ''

if int(user_list[-1]) == 1:
    percent = 'процент'
elif int(user_list[-1]) in range(2, 5):
    percent = 'процента'
elif int(user_list[-1]) in range(5, 21) or int(user_list[-1]) == 0:
    percent = 'процентов'

print(f'{user_number} {percent}')