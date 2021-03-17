class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
            return True
        return False

    def set_surname(self, surname):
        if isinstance(surname, str):
            self.surname = surname
            return True
        return False

    def __str__(self):
        return '"{0} {1}".'.format(self.name, self.surname)


class Guest(Person):
    def __init__(self, name, surname, city, role):
        Person.__init__(self, name, surname)
        self.city = city
        self.role = role

    def get_city(self):
        return self.city

    def get_role(self):
        return self.role

    def set_city(self, city):
        if isinstance(city, str):
            self.city = city
            return True
        return False

    def set_role(self, role):
        if isinstance(role, str):
            self.role = role
            return True
        return False

    def __str__(self):
        return '{0} {1}, г. {2}, статус "{3}"'.format(self.name, self.surname, self.city, self.role)