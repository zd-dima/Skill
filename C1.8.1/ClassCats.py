
class cats:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def getname(self):
        return self.name

    def getsex(self):
        return self.sex

    def getage(self):
        return self.age

    def printcats(self):
        print(f"Имя: {self.name}, Пол: {self.sex}, Возраст: {self.age}")
