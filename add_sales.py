from sys import argv
name, arg_1 = argv

with open('Lesson_6/task_6_6.csv', 'a', encoding='utf-8') as f:
    f.write(f'{arg_1}\n')


