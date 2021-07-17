def thesaurus(*names):
    name_dict = {}
    for name in names:
        name_dict.setdefault(f'{name[0]}', list())
        if name[0] in name_dict:
            name_dict[name[0]].append(name)
        else:
            name_dict[name[0]] = name
    return name_dict


print(thesaurus("Маша", "Иран", "Измир", "Рубин",  "Распутин", "Даша", "Дровосек", "Делениенаноль", "Афродита"))
