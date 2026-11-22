goods = [
    ["A1", "кеды", 2500],
    ["A2", "ботинки", 4800],
    ["A3", "сандалии", 1900]
]
print("1 — Войти как гость")
print("0 — Выход")
choice = input("Команда: ")

if choice == "1":
    print("Гость")
    for item in goods:
        print(item[0], "—", item[1], "—", item[2], "руб.")
elif choice == "0":
    print("Работа завершена")
else:
    print("Неверная команда")
