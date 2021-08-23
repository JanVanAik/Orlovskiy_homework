from itertools import zip_longest


class Matrix:
    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        result = []
        for i in range(len(self.list)):
            result.append([])
            for j in range(len(self.list[i])):
                result[i].append(self.list[i][j] + other.list[i][j])
        res = ''
        for i in range(len(result)):
            res +='  '.join(map(str, result[i]))
            res +='\n'
        return res


m_1 = [[1, 3, 5], [2, 6, 9], [2, 9, 11]]
m_2 = [[1, 7, 7], [3, 4, 7], [3, 5, 8]]

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
print(matrix_1 + matrix_2)