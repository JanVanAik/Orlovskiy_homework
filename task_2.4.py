names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# версия с созданием списка
for i in names:
    check_list = i.split(" ")
    for n in check_list:
        check_list[-1] = check_list[-1].title()
    print(f'Привет, {check_list[-1]}!')

    i = " ".join(check_list)

# версия без создания нового списка
for i in names:
    print(f'Привет, {i.split(" ")[-1].title()}!')
