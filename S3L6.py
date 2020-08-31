class Worker:

    def __init__(self, name, surname, position, _income, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, _income, bonus):
        super().__init__(name, surname, position, _income, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_total_income(self):
        self.__income = {'wage': self._income, 'bonus': self.bonus}
        return self.__income

seller = Position('Ivan', 'Ivanov', 'seller', 25000, 5000)
print(seller.get_full_name(), seller.get_total_income())