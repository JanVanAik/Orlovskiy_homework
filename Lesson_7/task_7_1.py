import os
dirs = ['settings', 'mainapp', "adminapp", 'authapp']
for i in dirs:
    os.makedirs(f"my_project/{i}")