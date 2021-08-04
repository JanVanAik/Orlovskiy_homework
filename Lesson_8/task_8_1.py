import re

email_list = ['12345@gmail.com', 'Hello@biz.com', 'Python@yandex.ru', 'Tema@tema.ru',
              'welcometopython@python.org', 'ololomis@take@pochta.ru.ru', 'randomtext@']


def email_parse(email):
    result = {
        "username": None,
        "domain": None
    }
    re_email = re.compile(r'([\w]+)@([\w]+\.\w+)', re.IGNORECASE)
    if re_email.match(email):
        splitted = re.split(r'@', email)
        result["username"] = splitted[0]
        result['domain'] = splitted[1]
        return result
    else:
        raise ValueError


    splitted = re.split(r'@', email)
    result["username"] = splitted[0]
    result['domain'] = splitted[1]
    return result


for num in email_list:
    try:
        print(email_parse(num))
    except ValueError:
        print('Wrong email')