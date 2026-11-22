orders = {
    "Z1": "Новый",
    "Z2": "Готов",
    "Z3": "Выдан"
}
role = input("Роль: ").lower()
sku = input("Артикул заказа: ")

if role != "администратор":
    print("Удаление заказов запрещено")
elif sku not in orders:
    print("Заказ не найден")
else:
    del orders[sku]
    print("Обновлённый список:")
    for key in orders:
        print(key, "—", orders[key])
