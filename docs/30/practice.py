orders = [
    ["Z1", "Новый", "Север"],
    ["Z2", "Готов", "Центр"],
    ["Z3", "Выдан", "Юг"]
]
running = True

while running:
    print("Главное меню")
    print("1 — Заказы")
    print("0 — Выход")
    choice = input("Команда: ")

    if choice == "1":
        in_list = True
        print("Список заказов:")
        for order in orders:
            print(order[0], "—", order[1], "—", order[2])
        while in_list:
            back = input("Введите Назад или 0 для выхода: ").lower()
            if back == "назад":
                in_list = False
            elif back == "0":
                in_list = False
                running = False
                print("Работа завершена")
            else:
                print("Неверная команда")
    elif choice == "0":
        running = False
        print("Работа завершена")
    else:
        print("Неверная команда")
