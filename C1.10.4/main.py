from clients import Guest

guests = [
Guest("Иван", "Иваныч", "Москва", "Наставник"),
Guest("Сергей", "Иваныч", "Мытищи", "Наставник"),
Guest("Василий", "Петрович", "Санкт-Петербург", "Наставник")
]

print("\nСписок гостей:")
for guest in guests:
    print(guest)