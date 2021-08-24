
class Storage:
    front_office = {}
    secondary_office = {}
    global_storage = {
        'Printer': [],
        'Scaner': [],
        'Xerox': []
    }
    shop = {}


class Tech:
    def __init__(self, voltage, ppm, height, amount=1):  # ppm = page per minute
        self.voltage = voltage
        self.ppm = ppm
        self.height = height
        self.amount = amount


    def to_storage(self, type_name, room=Storage.global_storage):
        for k, v in room.items():
            params = self.__dict__
            if k == type_name:
                room[k].append(params)




    @staticmethod
    def is_valid(obj):
        pass

class Printer(Tech):
    def __init__(self, voltage, ppm, height, amount, color_amount):
        super().__init__(voltage, ppm, height, amount)
        self.color_amount = color_amount


class Xerox(Tech):
    def __init__(self, voltage, ppm, height, amount, page_size):
        super().__init__(voltage, ppm, height, amount)
        self.page_size = page_size


class Scanner(Tech):
    def __init__(self, voltage, ppm, height, amount, color):
        super().__init__(voltage, ppm, height, amount)
        self.color = color


m_1 = Printer(220, 30, 30, 5, 15)
m_2 = Xerox(220, 15, 5, 1, 5)
m_3 = Scanner(330, 10, 5, 3, 8)
print(m_1.__dict__)
print(Printer.__name__)
print(m_1.voltage)
print(m_2.page_size)
print(m_3.color, m_3.ppm, m_3.height)
m_1.to_storage('Printer')
m_2.to_storage('Xerox')
m_3.to_storage('Printer')
print(Storage.global_storage)

