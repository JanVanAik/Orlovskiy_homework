class Worker:
    income_inlib = {
        "wage": 5000,
        "bonus": 1000
    }

    def __init__(self, name, surname, pos, income=income_inlib):
        self.name = name
        self.surname = surname
        self.position = pos
        self.__income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_income(self):
        full_income = self.income_inlib["wage"] + self.income_inlib["bonus"]
        return full_income



a = Position("Ivan", "Ivanov", "Head Engineer")
print(a.get_full_income())

print(a.get_full_name())
print(a.income_inlib)

