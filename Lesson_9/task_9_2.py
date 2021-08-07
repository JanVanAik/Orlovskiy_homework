class Road:

    def __init__(self, length, width, weight, deep):
        self._length = length
        self._width = width
        self.weight = weight
        self.deep = deep


    def count_asphalt(self):
        res = self.weight * self._length * self._width * self.deep / 1000
        return str(int(res)) + ' tons'

counter = Road(150, 10, 20, 30)
print(counter.count_asphalt())

counter2 = Road(150, 10, 10, 10)
counter2._length = 1000
counter2._width = 111
print(counter2.count_asphalt())

checkup = Road(150, 10, 44, 130)
print(checkup.count_asphalt())