goods = {
    "A1": "кеды",
    "A2": "ботинки",
    "A3": "сандалии"
}
sku = input("Артикул товара: ")

if sku not in goods:
    print("Товар не найден")
else:
    answer = input("Удалить? (да/нет): ").lower()
    if answer == "да":
        del goods[sku]
        print("Оставшийся каталог:")
        for key in goods:
            print(key, "—", goods[key])
    elif answer == "нет":
        print("Удаление отменено")
    else:
        print("Ошибка: ответ должен быть да или нет")
