orders = {
    "Z1": "Новый",
    "Z2": "Готов",
    "Z3": "Выдан"
}
sku = input("Артикул заказа: ")
status = input("Новый статус: ")

if sku not in orders:
    print("Заказ не найден")
elif status != "Новый" and status != "Готов" and status != "Выдан":
    print("Недопустимый статус")
else:
    orders[sku] = status
    print("Артикул:", sku)
    print("Статус:", orders[sku])
