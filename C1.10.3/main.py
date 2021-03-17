from clients import Client

print()
client_1 = Client("Семен", "Семеныч")
print(client_1)
client_1.add_money(50)
print(client_1.get_account())
client_1.add_money(10.5)
client_1.spend_money(5)

print()
print(client_1)
print("Транзакции клиента: ", ", ".join(map(str, client_1.get_transactions())))