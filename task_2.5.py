prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11,
          45.78, 48.29,  8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
correct_prices = []
# Пункт А - вывод списа и добавление "0" к копейкам
for i in prices:
    rub = int(i//1)
    kop = round(i % 1 * 100)
    if int(kop) < 10:
        kop = f'0{kop}'
        correct_prices.append(f'{rub} руб, {kop} коп')
print(correct_prices)
# Пункт В - сортировка по возрастанию in place,  с выводом id для доказательства
print(id(correct_prices))
correct_prices.sort()
print(correct_prices)
print(id(correct_prices))
# Пункт С - сортировка по убыванию, но в новом элементе, id для сравнения
correct_prices_reversed = list(reversed(correct_prices))
print(correct_prices_reversed)
print(id(correct_prices_reversed))
# Пункт D - вывод цены пяти самых дорогих товаров
print(f'{list(reversed(correct_prices_reversed[:5]))}')
