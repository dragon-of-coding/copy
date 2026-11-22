orders = [
    ["Z1", "Новый", "Север"],
    ["Z2", "Готов", "Центр"],
    ["Z3", "Выдан", "Юг"]
]
role = input("Роль: ").lower()

if role == "менеджер" or role == "администратор":
    for order in orders:
        print("Артикул:", order[0])
        print("Статус:", order[1])
        print("Пункт выдачи:", order[2])
        print("---")
else:
    print("Просмотр заказов недоступен")
