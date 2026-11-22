orders = [
    ["Z1", "Новый", "Север"],
    ["Z2", "Готов", "Центр"],
    ["Z3", "Выдан", "Юг"]
]
sku = input("Артикул заказа: ")
pickup = input("Новый пункт выдачи: ").strip()
found = False

for order in orders:
    if order[0] == sku:
        found = True
        if pickup != "":
            order[2] = pickup

if found == False:
    print("Заказ не найден")
elif pickup == "":
    print("Ошибка: пустой пункт выдачи")
else:
    for order in orders:
        print(order[0], "—", order[1], "—", order[2])
