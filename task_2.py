base_list = []
for i in range(1, 1001):
    if i % 2 == 1:
        i = i ** 3
        base_list.append(i)

for i in base_list:
    sum_check = 0
#Ввожу num, чтобы иметь возможность производить с числом манипуляции
    num = i
    while num > 0:
        sum_check += num % 10
        num = num // 10
    if sum_check % 7 == 0:
        sum = sum + i
print(sum)
#Задание со *
# Код аналогичен предыдущему, прорсто в переборе добавляем 17 к каждому числу перед проверкой суммы цифр
sum = 0
for i in base_list:
    i += 17
    sum_check = 0
    num = i
    while num > 0:
        sum_check += num % 10
        num = num // 10
    if sum_check % 7 == 0:
        sum = sum + i
print(sum)





