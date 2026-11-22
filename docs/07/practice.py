users = {
    "client": ["111", "клиент"],
    "manager": ["222", "менеджер"],
    "admin": ["333", "администратор"]
}
login = input("Логин: ")
password = input("Пароль: ")

if login in users and users[login][0] == password:
    role = users[login][1]
    print("Роль:", role)
    if role == "клиент":
        print("Просмотр товаров")
    elif role == "менеджер":
        print("Просмотр товаров, просмотр заказов")
    else:
        print("Просмотр и изменение товаров и заказов")
else:
    print("Доступ запрещён")
