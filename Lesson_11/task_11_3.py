class UserError(Exception):
    def __init__(self, text='Error, not a number'):
        self.text = text


user_input = ''
number_list = []
error_list = []
err_count = 0
while user_input != 'stop':
    user_input = input('Введите число,которое хотите добавить в список: ')
    try:
        if user_input.isdigit() == False:
            err_count +=1
            error_list.append(user_input)
            raise UserError
    except UserError:
        print('That is not a number, cant you read?')
    else:
        number_list.append(int(user_input))
        print(number_list)
    finally:
        print('If you are tired, just print "stop"')
print(f'Thanks for participating. Your final list is {number_list} \n'
      f'You typed some useless junk {err_count} times\nYour errors are {error_list}')