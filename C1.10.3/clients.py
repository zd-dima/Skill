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


class Client(Person):
    def __init__(self, name, surname, account=0):
        Person.__init__(self, name, surname)
        self.account = account
        self.transactions = [account]

    def get_account(self):
        return self.account

    def get_transactions(self):
        return self.transactions.copy()

    def spend_money(self, amount):
        if isinstance(amount, (int, float)) and (0 <= amount <= self.account):
            self.account -= amount
            self.transactions.append(-amount)
            return True
        return False

    def add_money(self, amount):
        if isinstance(amount, (int, float)) and (amount >= 0):
            self.account += amount
            self.transactions.append(amount)
            return True
        return False

    def __str__(self):
        return 'Клиент "{0} {1}". Баланс: {2} руб.'.format(self.name, self.surname, self.account)