users = {
    "anna": "111",
    "ivan": "222",
    "olga": "333"
}
running = True

while running:
    login = input("Логин: ")
    password = input("Пароль: ")
    if login in users and users[login] == password:
        print("Личный кабинет")
        in_account = True
        while in_account:
            print("1 — Выйти из учётной записи")
            print("0 — Завершить программу")
            choice = input("Команда: ")
            if choice == "1":
                print("Выход из учётной записи")
                in_account = False
            elif choice == "0":
                print("Работа завершена")
                in_account = False
                running = False
            else:
                print("Неверная команда")
    else:
        print("Неверный логин или пароль")
