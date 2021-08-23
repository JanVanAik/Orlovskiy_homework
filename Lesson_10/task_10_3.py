class Cell:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        return f'{self.numbers}'

    def __add__(self, other):
        print('Sum: ')
        return Cell(self.numbers + other.numbers)

    def __sub__(self, other):
        if self.numbers - other.numbers >= 0:
            print('Diff: ')
            return Cell(self.numbers - other.numbers)
        else:
            return 'Input correct numbers'

    def __mul__(self, other):
        print('Multiply: ')
        return Cell(self.numbers * other.numbers)

    def __floordiv__(self, other):
        print('Div: ')
        return Cell(self.numbers//other.numbers)

    def make_order(self, amount):
        return '\n'.join(['*' * amount for i in range(self.numbers // amount)]) + '\n' + '*' * (self.numbers % amount)


a = Cell(15)
b = Cell(5)
c = Cell(77)
print(a.make_order(7))
print(Cell(a+b))
print(a-b)
print(a*b)
print(a//b)
print(a - c)
