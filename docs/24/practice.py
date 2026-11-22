orders = {
    "Z1": "Новый",
    "Z2": "Готов",
    "Z3": "Выдан"
}
sku = input("Артикул заказа для удаления: ")

if sku in orders:
    del orders[sku]
    print("Обновлённый список:")
    for key in orders:
        print(key, "—", orders[key])
    print("Осталось заказов:", len(orders))
else:
    print("Заказ не найден")
