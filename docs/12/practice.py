orders = [
    ["Z1", "Новый"],
    ["Z2", "Готов"],
    ["Z3", "Выдан"]
]
role = input("Роль: ").lower()
sku = input("Артикул нового заказа: ").strip()
exists = False

for order in orders:
    if order[0] == sku:
        exists = True

if role != "администратор":
    print("Добавление запрещено")
elif sku == "":
    print("Ошибка: пустой артикул")
elif exists:
    print("Ошибка: артикул уже существует")
else:
    orders.append([sku, "Новый"])
    for order in orders:
        print(order[0], "—", order[1])
