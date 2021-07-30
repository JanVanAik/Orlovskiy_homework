from sys import argv
name, *args = argv
with open('task_6_6.csv', 'r', encoding='utf-8') as f:
    i = 0
    if len(argv) == 1:
        for line in f:
            print(line.replace('\n', ''))
    elif len(argv) == 2:
        for i in range(1, 100):
            if i < int(argv[1]):
                f.readline()
                i += 1
            else:
                for line in f:
                    print(line.replace('\n', ''))
    elif len(argv) == 3:
        for i in range(1, 100):
            if i < int(argv[1]):
                f.readline()
                i += 1
            else:
                ff = f.readline()
                print(ff.replace('\n', ''))
                if i == int(argv[2]):
                    break
                else:
                    i+=1

