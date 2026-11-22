users = {
    "anna": ["111", "клиент"],
    "ivan": ["222", "менеджер"],
    "olga": ["333", "администратор"]
}
login = input("Логин: ")
password = input("Пароль: ")

if login in users:
    if users[login][0] == password:
        print("Вход выполнен")
        print("Роль:", users[login][1])
    else:
        print("Неверный логин или пароль")
else:
    print("Неверный логин или пароль")
