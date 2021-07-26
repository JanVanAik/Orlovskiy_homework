from itertools import zip_longest
with open('users.txt', 'r', encoding='utf-8') as us:
    with open('hobby.txt', 'r', encoding='utf-8') as hb:
        hobbies = []
        users = []
        for user in us.readlines():
            user = user.replace(",", " ").replace('\n', '')
            users.append(user)
        for hobby in hb.readlines():
            hobby = hobby.replace('\n', '')
            hobbies.append(hobby)
        result = {k: v for k, v in zip_longest(users, hobbies, fillvalue=None)}
        print(result)
