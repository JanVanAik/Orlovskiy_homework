import os

result = {100: 0,
          1000: 0,
          10000: 0,
          100000: 0,
          1000000: 0,
          10000000: 0,
          100000000: 0}
elem_count = 0

def count_size(element):
    for k in result.keys():
        if os.stat(element).st_size > k:
            pass
        else:
            result[k] += 1
            break

def recursive_opener(dir_path):
    global elem_count
    if os.path.isdir(dir_path):
        os.chdir(dir_path)
        for file in os.listdir():
            try:
                if os.path.isfile(file):
                    count_size(file)
                    elem_count += 1
                else:
                    recursive_opener(os.path.join(dir_path, file))
            except FileNotFoundError:
                pass
    else:
        count_size(dir_path)
        elem_count += 1


print(recursive_opener('/Users/Artem/PycharmProjects/Orlovskiy_homework/venv/'))
print(result)
print(elem_count)
