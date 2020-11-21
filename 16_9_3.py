class Customers:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_balance(self):
        return self.balance


customer_1 = Customers('Иван', 'Петров', 50)
print(f'Клиент "{customer_1.get_name()} {customer_1.get_surname()}". Баланс: {customer_1.get_balance()} руб')
