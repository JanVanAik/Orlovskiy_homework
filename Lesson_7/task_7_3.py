import os
import shutil
folder = '/Users/Artem/PycharmProjects/Orlovskiy_homework/my_project/'
if os.path.exists(f'{folder}/templates') is not True:
    os.mkdir(f'{folder}/templates')
for direct in os.listdir(path=folder):
    os.chdir(f"{folder}/{direct}")
    for file in os.listdir():
        if os.path.isdir(file) and file == 'templates':
            os.chdir(file)
            for element in os.listdir():
                shutil.copytree(element,
                                f'{folder}/templates/{element}')
                shutil.rmtree(f"{folder}/{direct}/templates")

