users = {
    "anna": ["111", "Анна Иванова"],
    "ivan": ["222", "Иван Петров"],
    "olga": ["333", "Ольга Смирнова"]
}
login = input("Логин: ")
password = input("Пароль: ")

if login == "" or password == "":
    print("Неверные учётные данные")
elif login in users:
    if users[login][0] == password:
        print("Здравствуйте,", users[login][1])
    else:
        print("Неверные учётные данные")
else:
    print("Неверные учётные данные")
