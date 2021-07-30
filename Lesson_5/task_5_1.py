def generator(gen_length):
    for num in range(1, gen_length):
        if num % 2 != 0:
            yield num


n = int(input('Введите n: '))
print(*generator(n))
