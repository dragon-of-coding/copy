import math

goods = [
    [1, "кеды", 2500],
    [2, "ботинки", 4800],
    [3, "сандалии", 1900]
]
name = input("Название: ").strip()
price_text = input("Цена: ")

if name == "":
    print("Ошибка: пустое название")
else:
    try:
        price = float(price_text)
        if price < 0 or math.isfinite(price) == False:
            print("Ошибка: цена должна быть неотрицательным числом")
        else:
            max_id = 0
            for item in goods:
                if item[0] > max_id:
                    max_id = item[0]
            goods.append([max_id + 1, name, price])
            for item in goods:
                print(item[0], "—", item[1], "—", item[2], "руб.")
    except ValueError:
        print("Ошибка: цена должна быть числом")
