orders = [
    ["Z1", "Новый", "Север"],
    ["Z2", "Готов", "Центр"],
    ["Z3", "Выдан", "Юг"]
]
sku = input("Артикул заказа: ")
found = False

for order in orders:
    if order[0] == sku:
        print("Артикул:", order[0])
        print("Статус:", order[1])
        print("Пункт выдачи:", order[2])
        found = True
        break

if found == False:
    print("Заказ не найден")
