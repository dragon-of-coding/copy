orders = [
    ["Z1", "Новый", "Центр"],
    ["Z2", "Новый", "Центр"],
    ["Z3", "Новый", "Центр"]
]
sku = input("Новый артикул: ").strip()
pickup = input("Пункт выдачи: ").strip()
exists = False

for order in orders:
    if order[0] == sku:
        exists = True

if sku == "":
    print("Ошибка: пустой артикул")
elif pickup == "":
    print("Ошибка: пустой пункт выдачи")
elif exists:
    print("Ошибка: артикул уже существует")
else:
    orders.append([sku, "Новый", pickup])
    for order in orders:
        print(order[0], "—", order[1], "—", order[2])
