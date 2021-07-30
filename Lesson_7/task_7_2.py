import yaml
import os
from pprint import pprint

def create_dir(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        print(f'Cannot create what already exists')

def create_file(path):
    my_file = open(path, 'w')
    my_file.close()


with open('Lesson_7/content.yaml', 'r', encoding='utf-8') as f:
    s = yaml.safe_load(f)
    pprint(s)
    for k, v in s.items():
        # Генерация первого уровня папок - my_project
        for key, val in v.items():
            # Генерация второго уровня папок - authapp, mainapp, settings
            create_dir(f'{k}/{key}')
            for file in val:
                if type(file) == dict:
                    for x, y in file.items():
                        # Генерация папок третьего уровня - templates
                        create_dir(f'{k}/{key}/{x}')
                        for n_file in y:
                            # Перебираем файлы в templates
                            if type(n_file) == dict:
                                for folder in n_file.keys():
                                    # Генерация папок четвертого уровня - authapp, mainapp
                                    create_dir(f'{k}/{key}/{x}/{folder}')
                                    for file_val in n_file.values():
                                        if type(file_val) == list:
                                            for u in file_val:
                                                # Генерация файлов пятого уровня - base.html, index.html
                                                create_file(f'{k}/{key}/{x}/{folder}/{u}')
                else:
                    # Генерация файлов 3 уровня - init.py, models.py, views.py
                    create_file(f'{k}/{key}/{file}')



