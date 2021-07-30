#Насколько я понимаю, идентичен task_6_3.py, т.к в третьем задании
# идет работа с readline, которая считывает данные по одной строке и не занимает значительную часть ОЗУ

from itertools import zip_longest
hobbies = []
users = []

with open('users.csv', 'r', encoding='utf-8') as us:
    with open('hobby.csv', 'r', encoding='utf-8') as hb:
         if len(us.readlines()) >= len(hb.readlines()):
            us.seek(0)
            hb.seek(0)
            for line in us:
                user = line.replace(",", " ").replace('\n', '')
                users.append(user)
            for line in hb:
                hobby = line.replace('\n', '')
                hobbies.append(hobby)
            result = {k: v for k, v in zip_longest(users, hobbies, fillvalue=None)}
            print(result)
         else:
            exit(1)
