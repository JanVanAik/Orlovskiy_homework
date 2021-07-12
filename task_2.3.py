meteorology = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# id до итераций, чтобы показать, что новый список не создавался
print(id(meteorology))
i = 0
while i < len(meteorology):
    num = meteorology[i]
    if num.isdigit() is True:
        if int(num) < 10:
            meteorology[i] = f'"0{num}"'
        else:
            meteorology[i] = f'"{num}"'
    if num.startswith("+") is True:
        num = num.replace('+', '')
        if int(num) < 10:
            meteorology[i] = f'"+0{num}"'
        else:
            meteorology[i] = f'+{num}'
    if num.startswith("-") is True:
        num = num.replace('-', '')
        if int(num) < 10:
            meteorology[i] = f'"-0{i}"'
        else:
            meteorology[i] = f'-{i}'
    i += 1

# id после итераций, чтобы показать, что новый список не создавался
print(id(meteorology))
print(" ".join(meteorology))
