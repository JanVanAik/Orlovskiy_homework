meteorology = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in meteorology:
    if i.isdigit() is True:
        if int(i) < 10:
            i = f'"0{i}"'
        else:
            i = f'"{i}"'
    if i.startswith("+") is True:
        i = i.replace('+', '')
        if int(i) < 10:
            i = f'"+0{i}"'
        else:
            i = f'+{i}'
    if i.startswith("-") is True:
        i = i.replace('-', '')
        if int(i) < 10:
            i = f'"-0{i}"'
        else:
            i = f'-{i}'
    print(f'{i} ', end='')
