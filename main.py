class Bank:
    def __init__(self, name, head_name, coef):
        self.name = name
        self.head_name = head_name
        self.__coef = coef

    @property
    def coef(self):
        return self.__coef

    @coef.setter
    def coef(self, value):
        if 0.0 <= value <= 100.0:
            self.__coef = value
        else:
            raise ValueError("коеф нормальный надо")

    def calculate(self, client, n):
        money = client.money
        money_after_n_years = money * (1 + self.coef) ** n
        return money_after_n_years


class Client:
    def __init__(self, name, id, bank, money):
        self.name = name
        self.id = id
        self.bank = bank
        self.__money = money
        self.__money_after_year = None

    @property
    def money(self):
        return self.__money

    @property
    def money_after_year(self):
        if self.__money_after_year is None:
            self.__money_after_year = self.bank.calculate(self, 1)
        return self.__money_after_year

    def invest(self, amount):
        if amount <= 0:
            print("Amount должен быть положительным")
        else:
            self.__money += amount

    def take_money(self, amount):
        if amount <= 0:
            print("Amount должен быть положительным")
        elif self.__money < amount:
            print("нет денег")
        else:
            self.__money -= amount


bank = Bank("Kaspi", "Lomtadze", 10)
client = Client("Shakhrukh", "10", bank, 1500000)

print(client.money)
print(client.money_after_year)

client.invest(320)
print(client.money)
print(client.money_after_year)

client.take_money(2500)
client.take_money(-500)
print(client.money)
print(client.money_after_year)

bank.coef = 6
print(client.money_after_year)