class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Имя, Фамилия: {self.name} {self.surname}'

    def get_full_profit(self):
        return f'Доход: {sum(self._income.values())} $'


manager_1 = Position('Andrew', 'Willson', 'CEO', 4000, 3000)
print(manager_1.get_full_name())
print(manager_1.get_full_profit())
print(manager_1.position)
