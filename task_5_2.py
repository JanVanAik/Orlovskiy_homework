n = int(input('Введите n: '))
nums = (num for num in range(1, n) if num % 2 != 0)
print(*nums)
