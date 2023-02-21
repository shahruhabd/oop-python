class Bank:
    def __init__(self, name, head_name, coef, money):
        self.name = name
        self.head_name = head_name
        self.__coef = coef
        self.money = None


### не понял суть свойства coef
    @property
    def get_coef(self):
        return self.__coef

    coef = property(get_coef)

    def calculate(self, n=1):
        return Client(self.money) * (n + self.__coef) ** n


class Client(Bank):
    def __init__(self, name, id, bank, money_after_year, head_name, coef):
        super().__init__(name, head_name, coef)
        self.name = name
        self.id = id
        self.bank = bank
        self.__money = self.money
        self.__money_after_year = None

    @property
    def money(self):
        return f'Ваш баланс ${self.money}'

    @property
    def money_after_year(self):
        return Bank.calculate(self, n=1)

    def invest(self, amount):
        if amount > 0:
            return self.money + amount
        else:
            f'нельзя вводить отрицательное число'

    def take_money(self, amount):
        if self.money > 0 and amount > 0:
            return self.money - amount
        else:
            f'нельзя вводить отрицательное число'


bank1 = Bank('Kaspi', 'Mikhail Lomtadze', 0.1, 1000)
print(bank1.calculate())
