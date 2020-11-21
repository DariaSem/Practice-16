class GuestList:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class ExtendedList(GuestList):
    def __init__(self, name, city, status):
        super().__init__(name)
        self.city = city
        self.status = status

    def get_city(self):
        return self.city

    def get_status(self):
        return self.status


guest_1 = ExtendedList('Иван Петров', 'Москва', 'Наставник')
print(f'"{guest_1.get_name()}, г. {guest_1.get_city()}, статус "{guest_1.get_status()}"')
